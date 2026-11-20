from PIL import Image, ImageDraw
global raw_rgb_bytes
text = input("String>> ")
format = input("RGB or BMP>> ").lower().strip()
dev = input("would you like a .h file? y / n>> ").lower().strip()
#creating the file
img = Image.new("RGB", (200, 50), color=(0, 0, 0))
draw = ImageDraw.Draw(img)
#DRawing
draw.text((10, 15), text, fill=(255, 255, 255))
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
