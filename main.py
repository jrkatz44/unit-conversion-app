from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
	return {"message": "Welcome to the Unit Conversion App"}


@app.get("/convert")
def convert_units(value: float, from_unit: str, to_unit: str):
	#placeholder conversion logic 
	return {
		"input_value": value,
		"from_unit": from_unit,
		"to_unit": to_unit,
		"converted_value": value # we'll replace this with actual logic later 
	}