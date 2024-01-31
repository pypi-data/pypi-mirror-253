import pytest
from chinchilla import Chinchilla


@pytest.mark.parametrize("valid_param_grid", [0], indirect=True)
@pytest.mark.parametrize("valid_seed_ranges", [0], indirect=True)
# @pytest.mark.parametrize("valid_model_search_config", [0], indirect=True)
@pytest.mark.parametrize("project_dir", ["examples/efficientcube-1e14_1e15--mlp"])
@pytest.mark.parametrize(
    "method_name, args, kwargs",
    [
        # ("seed", ()),
        ("scale", (), {}),
        ("scale", (), dict(C=5.73e21, scaling_factor=3)),
        ("step", (99,), {}),
        # ("plot", ()),
    ],
)
def test_method(project_dir, method_name, args, kwargs, valid_param_grid, valid_seed_ranges):
    print(method_name, args, kwargs)
    with pytest.raises(ValueError):
        cc = Chinchilla(
            project_dir,
            param_grid=valid_param_grid,
            seed_ranges=valid_seed_ranges,
            # model_search_config=valid_model_search_config,
            log_level=20,
        )
        getattr(cc, method_name)(*args, **kwargs)


def test_no_dir():
    with pytest.raises(ValueError):
        import numpy as np
        cc = Chinchilla(
            # "examples/demo",
            None,
            param_grid=dict(
                e=np.linspace(1.3, 1.3, 1),
                A=np.linspace(100, 400, 4),
                B=np.linspace(100, 400, 4),
                alpha=np.linspace(0.3, 0.5, 3),
                beta=np.linspace(0.3, 0.5, 3),
            ),
            seed_ranges=dict(C=(1e21, 1e29), N_to_D=(10, 40)),
            log_level=20,
            scaling_factor=10,
        )
