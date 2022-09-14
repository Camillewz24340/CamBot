import discord
import qrcode

def makeqr(d:any):

    """
    d = data
    """

    QRCode = qrcode.make(str(d))

    file = QRCode.save("data/TempData/QrCode/qr.png")

    return discord.File("data/TempData/QrCode/qr.png")