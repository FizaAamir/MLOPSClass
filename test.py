from main import Bulb

bulb=Bulb()
def test_bulb_isOff():
    assert bulb.getstatus()=="Bulb id not glowing"
    

def test_bulb_isOn():
    bulb.ison()
    assert bulb.getstatus()=="Bulb is glowing"
    
def test_getStatus():
   bulb.isOff()
   assert bulb.getStatus()="Bulb is not Glowing"

print("Hello World Hello World")
prinf("Hi")


