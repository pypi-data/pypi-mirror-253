import time

import numpy as np
from taurex.optimizer import Optimizer
from taurex.util.util import recursively_save_dict_contents_to_output
from .autoemcee import ReactiveAffineInvariantSampler


class EmceeSampler(Optimizer):
    """
    Emcee sampler for TauREx3.1.

    Parameters
    ----------
    observed: :class:`~taurex.data.spectrum.spectrum.BaseSpectrum`, optional
        Sets the observation to optimize the model to
    model: :class:`~taurex.model.model.ForwardModel`, optional
        The forward model we wish to optimize
    sigma_fraction: float, optional
        Fraction of weights to use in computing the error. (Default: 0.1)
    num_global_samples: int
        Number of samples to initially draw from the prior. Default is 10000
    num_chains: int
        Number of independent ensembles to run. Default is 4
    num_walkers: int
        Ensemble size. Default is max(100, 4 * dim)
    max_ncalls: int
        Maximum number of likelihood function evaluations. Default is 1000000
    growth_factor: int
        Factor by which to increase the number of steps. Default is 10
    max_improvement_loops: int
        Number of times MCMC should be re-attempted. Default is 4
    num_initial_steps: int
        Number of sampler steps to take in first iteration. Default is 100
    min_autocorr_times: int
        If positive, sets autocorelation as an additional convergence criterion. Default is 0
    rhat_max: float
        Sets Gelman-Rubin diagnostic to converge. Default is 1.01
    geweke_max: float
        Sets Gelman-Rubin diagnostic to converge. Default is 2.0
    progress: bool
        If True, show progress bars. Default is True
    """

    def __init__(
        self,
        observed=None,
        model=None,
        sigma_fraction: float = 0.1,
        num_global_samples=10000,
        num_chains=4,
        num_walkers=None,
        max_ncalls=1000000,
        growth_factor=10,
        max_improvement_loops=4,
        num_initial_steps=100,
        min_autocorr_times=0,
        rhat_max=1.01,
        geweke_max=2.0,
        progress=True,
    ):
        super().__init__("Emcee", observed, model, sigma_fraction)

        self.num_global_samples = int(num_global_samples)
        self.num_chains = int(num_chains)
        self.num_walkers = (
            int(num_walkers) if num_walkers else None
        )  # If None, max(100, 4 * dim) is used
        self.max_ncalls = int(max_ncalls)
        self.growth_factor = int(growth_factor)
        self.max_improvement_loops = int(max_improvement_loops)
        self.num_initial_steps = int(num_initial_steps)
        self.min_autocorr_times = min_autocorr_times
        self.rhat_max = float(rhat_max)
        self.geweke_max = float(geweke_max)
        self.progress = progress

    def compute_fit(self):
        data = self._observed.spectrum
        datastd = self._observed.errorBar
        sqrtpi = np.sqrt(2 * np.pi)

        def emcee_loglike(params):
            # log-likelihood function called by emcee
            fit_params_container = np.array(params)
            chi_t = self.chisq_trans(fit_params_container, data, datastd)
            loglike = -np.sum(np.log(datastd * sqrtpi)) - 0.5 * chi_t
            return loglike

        def emcee_transform(params):
            # prior distributions called by emcee. Implements a uniform prior
            # converting parameters from normalised grid to uniform prior
            cube = []
            for idx, prior in enumerate(self.fitting_priors):
                cube.append(prior.sample(params[idx]))
            return np.array(cube)

        ndim = len(self.fitting_parameters)
        self.info("Number of dimensions {}".format(ndim))
        self.info("Fitting parameters {}".format(self.fitting_parameters))

        if self.num_walkers is None:
            self.num_walkers = max(100, 4 * ndim)

        t0 = time.time()

        sampler = ReactiveAffineInvariantSampler(
            self.fit_names,
            loglike=emcee_loglike,
            transform=emcee_transform,
        )

        sampler.run(
            num_global_samples=self.num_global_samples,
            num_chains=self.num_chains,
            num_walkers=self.num_walkers,
            max_ncalls=self.max_ncalls,
            growth_factor=self.growth_factor,
            max_improvement_loops=self.max_improvement_loops,
            num_initial_steps=self.num_initial_steps,
            min_autocorr_times=self.min_autocorr_times,
            rhat_max=self.rhat_max,
            geweke_max=self.geweke_max,
            progress=self.progress,
        )

        t1 = time.time()
        self.info("Time taken to run 'Emcee' is %s seconds", t1 - t0)
        self.info("Fit complete.....")

        self.emcee_output = self.store_emcee_output(sampler.results)
        self.info("Output stored")

    def store_emcee_output(self, result):
        """
        This turns the output from emcee into a dictionary that can
        be output by TauREx

        Parameters
        ----------
        result: :obj:`dict`
            Result from an emcee sample call

        Returns
        -------
        dict
            Formatted dictionary for output

        """

        emcee_output = {}
        emcee_output["Stats"] = {}
        emcee_output["Stats"]["ncall"] = result["ncall"]
        emcee_output["Stats"]["converged"] = result["converged"]

        emcee_output["solution"] = {}
        emcee_output["solution"]["samples"] = result["samples"]
        emcee_output["solution"]["weights"] = np.ones(len(result["samples"])) / len(
            result["samples"]
        )
        emcee_output["solution"]["fitparams"] = {}

        posterior = result["posterior"]
        for idx, param_name in enumerate(self.fit_names):
            param = {}
            param["value"] = posterior["median"][idx]
            param["mean"] = posterior["mean"][idx]
            param["emcee_sigma"] = posterior["stdev"][idx]
            param["sigma_m"] = param["value"] - posterior["errlo"][idx]
            param["sigma_p"] = posterior["errup"][idx] - param["value"]
            param["trace"] = result["samples"][:, idx]

            emcee_output["solution"]["fitparams"][param_name] = param

        return emcee_output

    def get_samples(self, solution_idx):
        return self.emcee_output["solution"]["samples"]

    def get_weights(self, solution_idx):
        return self.emcee_output["solution"]["weights"]

    def write_optimizer(self, output):
        opt = super().write_optimizer(output)

        # num_global_samples (parameter, ...)
        opt.write_scalar("num_global_samples ", self.num_global_samples)
        opt.write_scalar("num_chains", self.num_chains)
        opt.write_scalar("num_walkers", self.num_walkers)
        opt.write_scalar("max_ncalls", self.max_ncalls)
        opt.write_scalar("max_improvement_loops", self.max_improvement_loops)
        opt.write_scalar("num_initial_steps", self.num_initial_steps)
        opt.write_scalar("min_autocorr_times", self.min_autocorr_times)

        return opt

    def write_fit(self, output):
        fit = super().write_fit(output)

        if self.emcee_output:
            recursively_save_dict_contents_to_output(output, self.emcee_output)

        return fit

    def chisq_trans(self, fit_params, data, datastd):
        res = super().chisq_trans(fit_params, data, datastd)

        if not np.isfinite(res):
            return 1e20

        return res

    def get_solution(self):
        """

        Generator for solutions and their
        median and MAP values

        Yields
        ------

        solution_no: int
            Solution number (always 0)

        map: :obj:`array`
            Map values

        median: :obj:`array`
            Median values

        extra: :obj:`list`
            Returns Statistics, fitting_params, raw_traces and
            raw_weights

        """

        names = self.fit_names
        opt_map = self.fit_values
        opt_values = self.fit_values
        for k, v in self.emcee_output["solution"]["fitparams"].items():
            # if k.endswith('_derived'):
            #     continue
            idx = names.index(k)
            # opt_map[idx] = v["map"]
            opt_values[idx] = v["value"]

        yield 0, opt_map, opt_values, [
            ("Statistics", self.emcee_output["Stats"]),
            ("fit_params", self.emcee_output["solution"]["fitparams"]),
            ("tracedata", self.emcee_output["solution"]["samples"]),
            ("weights", self.emcee_output["solution"]["weights"]),
        ]

    @classmethod
    def input_keywords(self):
        return [
            "emcee",
        ]

    BIBTEX_ENTRIES = [
        """
        @ARTICLE{2013PASP..125..306F,
               author = {{Foreman-Mackey}, Daniel and {Hogg}, David W. and {Lang}, Dustin and et al.},
                title = "{emcee: The MCMC Hammer}",
              journal = {\pasp},
             keywords = {Astrophysics - Instrumentation and Methods for Astrophysics, Physics - Computational Physics, Statistics - Computation},
                 year = 2013,
                month = mar,
               volume = {125},
               number = {925},
                pages = {306},
                  doi = {10.1086/670067},
        archivePrefix = {arXiv},
               eprint = {1202.3665},
         primaryClass = {astro-ph.IM},
               adsurl = {https://ui.adsabs.harvard.edu/abs/2013PASP..125..306F},
              adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
        """,
        """
        @ARTICLE{2010CAMCS...5...65G,
               author = {{Goodman}, Jonathan and {Weare}, Jonathan},
                title = "{Ensemble samplers with affine invariance}",
              journal = {Communications in Applied Mathematics and Computational Science},
             keywords = {Markov chain Monte Carlo, affine invariance, ensemble samplers},
                 year = 2010,
                month = jan,
               volume = {5},
               number = {1},
                pages = {65-80},
                  doi = {10.2140/camcos.2010.5.65},
               adsurl = {https://ui.adsabs.harvard.edu/abs/2010CAMCS...5...65G},
              adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
        """,
    ]
