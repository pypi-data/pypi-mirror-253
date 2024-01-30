(model_zoo)=
# Model Zoo 

| Model | Kooplearn Implementation | Notes |
| --- | :---: | --- |
| Ridge Regression {footcite:p}`Kostic2022`|  {class}`kooplearn.models.DMD` or <br>{class}`kooplearn.models.ExtendedDMD` | Full-rank models. Set `rank` to `None` at initialization. |
| Principal Component Regression {footcite:p}`Kostic2022`|  {class}`kooplearn.models.DMD`,<br>{class}`kooplearn.models.ExtendedDMD`,<br>{class}`kooplearn.models.KernelDMD`, or <br>{class}`kooplearn.models.NystroemKernel` | Low-rank models. Set `reduced_rank` to `False` at initialization. |
| Reduced Rank Regression {footcite:p}`Kostic2022`|  {class}`kooplearn.models.DMD`,<br>{class}`kooplearn.models.ExtendedDMD`,<br>{class}`kooplearn.models.KernelDMD`, or <br>{class}`kooplearn.models.NystroemKernel` | Optimal{footcite:p}`Kostic2022, Kostic2023SpectralRates` low-rank models. Set `reduced_rank` to `True` at initialization. |
| Randomized Solver {footcite:p}`Kostic2022`|  {class}`kooplearn.models.DMD`,<br>{class}`kooplearn.models.ExtendedDMD`, or<br>{class}`kooplearn.models.KernelDMD` | Set `svd_solver` to `'randomized'` at initialization. |
| Nyström Kernel Regression{footcite:p}`Meanti2023` | {class}`kooplearn.models.NystroemKernel` | |
| Hankel DMD {footcite:p}`Arbabi2017` | {class}`kooplearn.models.DMD`<br>{class}`kooplearn.models.ExtendedDMD`<br>{class}`kooplearn.models.KernelDMD` | Hankel DMD with an history of $m$ steps is obtained by fitting these models with dataset of context length $m + 1$ |
| VAMPNets{footcite:p}`Mardt2018, Wu2019` | {class}`kooplearn.models.DeepEDMD` + {class}`kooplearn.models.feature_maps.VAMPNet` | |
| DPNets{footcite:p}`Kostic2023DPNets` | {class}`kooplearn.models.DeepEDMD` + {class}`kooplearn.models.feature_maps.DPNet` | |
| Dynamic AutoEncoder{footcite:p}`Lusch2018, Morton2018` | {class}`kooplearn.models.DynamicAE` | When `use_lstsq_for_evolution == True`, the linear evolution of the embedded state is given by a least square model as in {footcite:t}`Morton2018`.|
| Consistent AutoEncoder{footcite:p}`Azencot2020CAE` | {class}`kooplearn.models.ConsistentAE` | |

```{footbibliography}
```