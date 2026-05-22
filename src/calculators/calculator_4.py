from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, reques: FlaskRequest) -> Dict:  # type:ignore
        body = reques.json
        input_data = self.__validate_body(body)

        average = self.__calculate(input_data)
        formated_response = self.__formated_responde(average)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        input_data = body["numbers"]
        return input_data

    def __calculate(self, numbers: List[float]) -> float:
        average_result = self.__driver_handler.average(numbers)
        return average_result

    def __formated_responde(self, average_result) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": average_result,
                "Success": True
            }
        }
