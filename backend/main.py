from typing import Optional

from fastapi import FastAPI

import CoolProp.CoolProp as CP

app = FastAPI()


@app.get("/pcrit/{fluid}")
def read_root(fluid: str):
    pressure_at_critical_point = CP.PropsSI(fluid,'pcrit')

    return {"pressure_at_critical_point": pressure_at_critical_point}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
