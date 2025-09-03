from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from typing import List

app = FastAPI()

@app.get("/ping")
def ping():
    return Response(content="pong", status_code=200, media_type="text/plain")


class Characteristic(BaseModel):
    max_speed: int
    max_fuel_capacity: int


class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

liste_cars: List[Car] = []

@app.post("/cars")
def create_car(new_car: List[Car]):
    liste_cars.extend(new_car)
    cars_serialized = [c.model_dump() for c in liste_cars]
    return JSONResponse(content=cars_serialized, status_code=201, media_type="application/json")

@app.get("/cars")
def all_cars():
    cars_serialized = [c.model_dump() for c in liste_cars]
    return JSONResponse(content=cars_serialized, status_code=200, media_type="application/json")

@app.get("/cars/{id}")
def car_by_id(id: str):
    for i, car in enumerate(liste_cars):
        if car.identifier == id:
            return JSONResponse(content=car[i], status_code=200, media_type="application/json")
    return Response(content="ID not found or doesn't exist", status_code="404", media_type="text/plain")


@app.put("/cars/{id}/characteristics")
def update_cars(id: int, max_speed: int, max_fuel_capacity: int):
    for i, car in enumerate(liste_cars):
        if car.identifier == id:
            car.characteristics





