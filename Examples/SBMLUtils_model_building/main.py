from sbmlutils.factory import *
from sbmlutils.metadata import *
from pathlib import Path

_m = Model(
    sid="model1",
    name="ExampleFromYoutube",
    notes="""
    # Example from Youtube channel
    This example illustrates how to use sbmlsim and sbmlutils
    """,
    compartments=[
        Compartment(sid="c", value=1.0, sboTerm=SBO.PHYSICAL_COMPARTMENT,
                    name='cytosol')
    ],
    species=[
        Species(sid="S1", compartment="c", initialConcentration=10.0,
                hasOnlySubstanceUnits=False, sboTerm=SBO.SIMPLE_CHEMICAL, name="glucose")
    ]
)

if __name__ == "__main__":
    create_model(
        _m,
        filepath=Path(__file__).parent / "result",
    )