from webcolors import name_to_rgb
from qrcode.main import QRCode


def get_rgb(color_name: str):
    obj = name_to_rgb(color_name)
    return obj.red, obj.green, obj.blue


def generate_qr(text, image_name, front_color: tuple, back_color: tuple):
    qr = QRCode()

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=front_color, back_color=back_color)
    img.save(file_name)
    print(f"QR code generated and file name {image_name}")


def main():
    user_input = input("Enter the text that you want to generate QR code:: ").strip()
    file_name = input("Enter the file name:: ").strip() + ".png"
    is_color = input("Do you want to change color of QR or not (y/n): ").lower()
    if is_color == "y":
        front_color_name = input("Enter front color name:: ").strip()
        back_color_name = input("Enter back color name:: ").strip()

        generate_qr(user_input, file_name, get_rgb(front_color_name), get_rgb(back_color_name))

    else:
        generate_qr(user_input, file_name, get_rgb("black"), get_rgb("white"))
        print("Invalid choice default qr code generated.")


if __name__ == "__main__":
    main()
