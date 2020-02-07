from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_manager.apps import fs_client


@api_view(["GET"])
def test_sessions(request):
    doc_ref = fs_client.collection("sessions").document("1")
    doc_ref.set({
            "id": 1,
            "visible_id": "1dacb2b7-8c06-4516-af8a-0f6bff8a76a5",
            "geo_id": 5454711,
            "name": "Albuquerque",
            "alternate_names": "ABQ, Al'bukerke, Albakrki, Albakerki, Albjukuehrokju, Albukerke, Albukerki, Albukerkė, Albukwer kwe, Albukwér kwé, Albuquerque, Alburquerque, Almpoukerki, Beeldil Daesenili *, Beeʼeldííl Dahsinil, Duke City, New Albuquerque, San Felipe de Neri, San Francisco Xavier, San Francisco de Albuquerque, The Duke City, Vokekyi Leuwi *, a bu kui ji, aelbeokeoki, alabakarki, alabukaraki, albakrky, albukark, albukarki, albukʼerkʼe, albwkrk  nyw myksykw, albwkrky, alpukerkki, arubakaki, Αλμπουκέρκη, Албакерки, Албакърки, Албукерки, Албюкуэрокю, Альбукерке, Ալբուկերկե, אלבקרקי, آلبوکرک، نیو میکسیکو, ألباكركي, البوکرکی, आल्बुकर्की, আলবাকার্কি, ਅਲਬੂਕਰਕੀ, ஆல்புகெர்க்கி, ಆಲ್ಬುಕರ್ಕ್, แอลบูเคอร์คี, ალბუკერკე, アルバカーキ, 阿布奎基, 앨버커키",
            "latitude": "35.08449",
            "longitude": "-106.65113999999998",
            "country_code": "US",
            "admin_code": "NM",
            "population": 559121,
            "elevation": "1511.0",
            "timezone": "America/Denver",
            "status": "initialized",
            "user_id": 321
        })
    return Response(status=status.HTTP_200_OK)
