"""Interactive Solara dashboard:  solara run app.py"""
from mesa.visualization import SolaraViz, make_plot_component, Slider
from speaking_out import NamingGameModel

model_params = {
    "seed": {"type": "InputText", "value": 42, "label": "Seed"},
    "n": Slider("Agents N", 1000, 100, 5000, 100),
    "k": Slider("Group size k", 3, 2, 40, 1),
    "beta": Slider("Social influence β", 0.5, 0.0, 1.0, 0.01),
    "p": Slider("Committed fraction p", 0.05, 0.0, 0.5, 0.005),
    "rule": {"type": "Select", "value": "unanimity",
             "values": ["unanimity", "union"], "label": "Agreement rule"},
    "interactions_per_step": Slider("Interactions / step", 100, 1, 2000, 10),
}

model = NamingGameModel()
page = SolaraViz(
    model,
    components=[make_plot_component(["n_A", "n_B", "n_AB"])],
    model_params=model_params,
    name="Higher-order naming game (Iacopini et al. 2022)",
)