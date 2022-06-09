
from django import template

from ..models import ImagesProduct, Category

register = template.Library()

# สามารถเพิ่มแบบ
# @register.filter   แบบนี้ไว้บนหัวฟังก์ชันก็ได้


# @stringfilter  # ทำให้รับเฉพาะ string ถ้าไม่ใช่ จะฟ้อง error

def getValueA(value):
    return value


def getOneImgProdID(prod_id):
    img = ImagesProduct.objects.filter(prod_id=prod_id).first()
    # print(prod_id)
    return img.images.url


def getCatFromProducts(lsProduct):
    return lsProduct[0].prod_category.cat_name


def getIdFromNameCat(cat):
    categorie = Category.objects.filter(cat_name=cat).first()
    return categorie.id


@register.filter
def getHtmlSliderImgs(idProduct):
    lstImg = ImagesProduct.objects.filter(prod_id=idProduct)
    ls = []
    for i, img in enumerate(lstImg):
        ls.append({'index': i+1, 'value': img, 'length': len(lstImg)})
    return ls


register.filter('getValueA', getValueA)
register.filter('getOneImgProdID', getOneImgProdID)
register.filter('getCatFromProducts', getCatFromProducts)
register.filter('getIdFromNameCat', getIdFromNameCat)
