modelImg = input("Img link of the model: ")
modelName = input("Name of the model: ")
modelPrice = input("Price of the model: ")
modelDes = input("Discription of the model: ")
modelFea = input("Feature of the model: ")
modelLink = input("Link of the model: ")
class Makecard:
  def __init__(self, img, name, price, des, fea, link):
    self.img = img
    self.name = name
    self.price = price
    self.des = des
    self.fea = fea 
    self.link = link
    

  def card(self):
      content = ("""<br/>
<div class="separator" style="clear: both; text-align: left;"><ul style="text-align: left;"><li><span style="font-family: courier; font-size: medium;"><b>{}</b></span></li></ul></div>
<div class="card">
  <img alt="{}" src="{}" style="width: 100%;" />
  <h1>{}</h1>
  <p class="price">{}/-</p><br />
  <p>
  {}
  </p><br />
  <p>
    <button onclick="window.open('{}','_blank');">
      buy now!
    </button>
  </p>
</div>""".format(self.fea,self.name,self.img,self.name,self.price,self.des,self.link))
      return (content)


p1 = Makecard(modelImg,modelName,modelPrice, modelDes,modelFea,modelLink )
data = p1.card()
print (data)


