from product.viewsets import foodViewset
from rest_framework  import routers


router=routers.DefaultRouter()
router.register("food",foodViewset)
