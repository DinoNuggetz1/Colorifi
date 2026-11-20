from PIL import Image, ImageDraw
global raw_rgb_bytes
col = (0,0,0)
text = input("String>> ")
format = input("RGB or BMP>> ").lower().strip()
dev = input("would you like a .h file? y / n>> ").lower().strip()
col = tuple(map(int, input("BColor as R,G,B>> ").split(",")))
tcol = tuple(map(int, input("TColor as R,G,B>> ").split(",")))
#creating the file
img = Image.new("RGB", (200, 50), color=col)
draw = ImageDraw.Draw(img)
#DRawing
draw.text((10, 15), text, fill=tcol)
if format == "bmp":
    img.save("output.bmp", format="BMP")
    print("Created output.bmp")
elif format == "rgb" and dev != 'y':
    raw_rgb_bytes = img.tobytes()
    with open("output.raw", "wb") as f:
        f.write(raw_rgb_bytes)
    print("Created output.raw")
elif dev == "y" and format == "rgb":
        raw_rgb_bytes = img.tobytes()
        bytes_per_line = 25
        c_array = ",\n".join(
            ", ".join(
                f"0x{byte:02X}"
                for byte in raw_rgb_bytes[start:start + bytes_per_line])
            for start in range(0, len(raw_rgb_bytes), bytes_per_line))
        with open("output.h", "w") as f:
            f.write("const unsigned int width = 200;\nconst unsigned int height = 50;\nconst unsigned char output[] = {\n")
            f.write(c_array)
            f.write("\n};\n")
        print("Created output.h")
else:
    print("unrecognized format")
