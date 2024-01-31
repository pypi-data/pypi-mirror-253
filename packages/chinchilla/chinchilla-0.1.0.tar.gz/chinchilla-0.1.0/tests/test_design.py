import pytest
import random
from chinchilla import Chinchilla
from chinchilla.simulator import Simulator


@pytest.mark.config
@pytest.mark.parametrize("config_path", ["examples/demo/config.yaml", "examples/demo/config.json"])
def test_from_config(config_path):
    _ = Chinchilla.from_config(config_path)


@pytest.mark.cc
@pytest.mark.parametrize("project_dir", ["examples/efficientcube-1e14_1e15--mlp"])
@pytest.mark.parametrize(
    "method_name, args",
    [
        ("seed", ()),
        # "scale",
        ("step", (128,)),
        ("plot", ()),
    ],
)
def test_method(project_dir, method_name, args, valid_param_grid, valid_seed_ranges, valid_model_search_config):
    cc = Chinchilla(
        project_dir,
        param_grid=valid_param_grid,
        seed_ranges=valid_seed_ranges,
        model_search_config=valid_model_search_config,
        log_level=20,
    )
    if method_name == "scale":
        cc.fit()
        cc.scale()
    else:
        # eval(f"cc.{method_name}()")
        getattr(cc, method_name)(*args)


@pytest.mark.sim
@pytest.mark.parametrize(
    ["project_dir", "target_params"],
    [
        ("examples/effective-LLM", dict(E=1.69337368, A=406.401018, B=410.722827, alpha=0.33917084, beta=0.2849083)),
        (
            "examples/efficientcube-1e14_1e15--mlp",
            dict(E=1.45, A=106.401018, B=110.722827, alpha=0.33917084, beta=0.2849083),
        ),
    ],
)
@pytest.mark.parametrize("valid_param_grid", [0], indirect=True)
@pytest.mark.parametrize("valid_seed_ranges", [0], indirect=True)
@pytest.mark.parametrize("valid_model_search_config", [0], indirect=True)
def test_simulate_scaling_object(
    project_dir, target_params, valid_param_grid, valid_seed_ranges, valid_model_search_config
):
    cc = Chinchilla(
        project_dir,
        param_grid=valid_param_grid,
        seed_ranges=valid_seed_ranges,
        model_search_config=valid_model_search_config,
    )
    cc.simulate(100, 0, target_params=target_params, noise_generator=(random.expovariate(4) for _ in iter(int, 1)))
    cc.simulate(
        100,
        1,
        scaling_factor=2,
        target_params=target_params,
        noise_generator=(random.expovariate(4) for _ in iter(int, 1)),
    )


@pytest.mark.skip
@pytest.mark.db
def test_append(valid_param_grid, valid_seed_ranges, valid_model_search_config):
    cc = Chinchilla(
        "fake",
        param_grid=valid_param_grid,
        seed_ranges=valid_seed_ranges,
        model_search_config=valid_model_search_config,
    )
    sim = Simulator(cc)
    sim.append(D=1, N=330, loss=1.0)
    sim.append(D=1, N=330, loss=2.0)
    sim.append(D=1, N=330, loss=0.0, a=0.10304)
    sim.append(D=1, N=330, loss=0.0, a=0.10304, b=987654)
    sim.append(D=1, N=330, loss=0.0)
