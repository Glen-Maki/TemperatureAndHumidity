import uvicorn
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import datetime
import DHT
import pigpio

app = FastAPI()

templates = Jinja2Templates(directory="templates")
jinja_env = templates.env

DHT_PIN = 4
sensor = None


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})


@app.get("/data")
def data():
    """温湿度値を返す"""
    try:
        data = sensor.read()
        today = datetime.datetime.fromtimestamp(
            data[0]).strftime("%Y/%m/%d %H:%M")
        status = data[2]
        temperature = data[3]
        humidity = data[4]
        if status == DHT.DHT_GOOD:
            dat = {"time": today, "temperature": temperature, "humidity": humidity}
            print(f"json: {dat}")
            return dat
        else:
            raise Exception(f"dht sensor error: {status}")
    except Exception as e:
        print(f"err: {str(e)}")

    return None


if __name__ == "__main__":
    pi = pigpio.pi()
    if not pi.connected:
        print(f"cannot connect to pigpio")
        exit()

    sensor = DHT.sensor(pi, DHT_PIN)
    # サーバ起動
    uvicorn.run(app, host="0.0.0.0", port=8000)

    sensor.cancel()
    print(f"cancelling")
    pi.stop()
