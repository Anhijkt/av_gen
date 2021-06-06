from gen import rule_gen
from PIL import Image, ImageDraw
from fastapi import FastAPI
from fastapi.responses import Response
from io import BytesIO

app = FastAPI()


@app.get("/hash/{hash_str}")
async def read_item(hash_str: str) :
	if len(hash_str) != 32 :
		return {"this must be a md5 hash"}
	field = await rule_gen(hash_str.lower())
	image = Image.new("RGB", (430,430), (0,0,0,0))
	draw = ImageDraw.Draw(image)
	y_pos = 0
	for i in field :
		x_pos = 0
		for j in i :
			if j :
				draw.rectangle([x_pos, y_pos, x_pos+20, y_pos+20], fill="black")
			else :
				draw.rectangle([x_pos, y_pos, x_pos+20, y_pos+20], fill="white")
			x_pos += 10
		y_pos += 10

	with BytesIO() as output:
		image.save(output, format="JPEG")
		contents = output.getvalue()
		return Response(contents, media_type="image/jpeg")


@app.get("/")
async def index() :
	return {"so this is a basic api that takes in a hash(/hash/{hash_str}) and returns you a image for avatar"}