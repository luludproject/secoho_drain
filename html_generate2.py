import openpyxl
import os
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance, ImageOps, ImageFilter



image_urls = [
	"https://velog.velcdn.com/images/unvillage7777/post/fa9ff8d2-8dda-482c-905c-ef330d96ffee/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/46e2b48d-4d3f-4763-968e-0699ccdafe7c/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/0911feb9-9f98-4790-a4c5-16ffa0aaba49/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/eb71da7b-319d-4154-999a-280b88ab02c4/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/8750efe3-c08f-4494-9b81-b4f535ca5291/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/16449d87-eb93-42c4-ae32-369cab1e5c3d/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/27bc9cdb-1c5c-42b0-bec9-d8714a5e1ddf/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/1f3ba523-b503-4b58-9bcf-a6614d478c7a/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/032dd6fe-7647-4f0c-8b18-c4a197209343/image.png",
    "https://velog.velcdn.com/images/unvillage7777/post/00906a6d-e413-4c65-8429-79f43085cb0a/image.png",
]


# 기본 디렉토리 설정
temp_dir = "이미지/"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# 랜덤으로 조정된 이미지 목록 가져오기
adjusted_images = os.listdir(temp_dir)

excel_file = '서초구.xlsx'
df = pd.read_excel(excel_file)


# HTML 템플릿
html_template = """
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>{sep_keyword11}</title>
        <meta content="width=device-width, initial-scale=1.0" name="viewport">
        <meta content="{sep_keyword11}, {sep_keyword44}, {sep_keyword55}, {sep_keyword66}, 서초구하수구막힘, 서초구싱크대막힘, 서초구변기막힘" name="keywords">
        <meta content="{sep_keyword11} 지금 바로 출동합니다. 📞 1555-5492" name="description">
        <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
        <link rel="profile" href="https://gmpg.org/xfn/11">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="{sep_keyword11}">
        <meta property="twitter:image" content="../이미지/{image_url}">
        <meta name="twitter:description" content="{sep_keyword11} 지금 바로 출동합니다. 📞1555-5492">
        <link rel="canonical" href="https://seocho.the-drain.com/blog/{sep_keyword0}">
        <meta property="og:locale" content="ko_KR">
        <meta property="og:type" content="article">
        <meta property="og:title" content="{sep_keyword11}">
        <meta property="og:description" content="{sep_keyword11} 지금 바로 출동합니다. 📞1555-5492">
        <meta property="thumbnail" content="../이미지/{image_url}">
        <meta property="og:url" content="https://seocho.the-drain.com/blog/{sep_keyword0}">
        <meta property="og:site_name" content="{sep_keyword66}">
        <meta property="og:image" content="../이미지/{image_url}">
        <meta property="og:image:secure_url" content="../이미지/{image_url}">
        <meta property="og:image:width" content="500">
        <meta property="og:image:height" content="500">
        <meta property="og:image:alt" content="하수구막힘">
        <meta property="og:image:type" content="image/png">
        <link href="../img/favicon.ico" rel="icon">
        <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/moonspam/NanumSquare@2.0/nanumsquare.css">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
        <link href="../lib/animate/animate.min.css" rel="stylesheet">
        <link href="../lib/flaticon/font/flaticon.css" rel="stylesheet"> 
        <link href="../lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
        <link href="../lib/lightbox/css/lightbox.min.css" rel="stylesheet">
        <link href="../css/style.css" rel="stylesheet">
        <meta property="article:published_time" content="2025-09-18T06:00:00+09:00" />
        <meta property="article:modified_time" content="2025-09-18T06:00:00+09:00" />

        <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "✅ {sep_keyword66} 해결 방법이 어떻게 되나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "기본장비부터 고가의 고압세척 장비와
        10년 이상의 전문가들로 빠르고 깔끔하게 하수구 막힘을 해결해드립니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "✅ 지역은 어디까지 출장이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "저희 더 드레인은 365일 24시 서울/인천/경기 어디든 작업이 가능합니다. 👉🏼 1555-5492"
      }}
    }}
  ]
}}
</script>
    </head>

    <body>
        <div class="top-bar d-none d-md-block">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-8">
                        <div class="top-bar-left">
                            <div class="text">
                                <i class="far fa-clock"></i>
                                <h2>24시간 운영중</h2>
                                <p>월 ~ 일</p>
                            </div>
                            <div class="text">
                                <i class="fa fa-phone-alt"></i>
                                <h2>1555 - 5492</h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="navbar navbar-expand-lg bg-dark navbar-dark">
            <div class="container-fluid">
                <a href="/" class="navbar-brand">서초구하수구막힘</a>
                <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse justify-content-between" id="navbarCollapse">
                    <div class="navbar-nav ml-auto">
                        <a href="/" class="nav-item nav-link active">홈</a>
                        <a href="/service" class="nav-item nav-link active">서비스</a>
                        <a href="/blog" class="nav-item nav-link active">블로그</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="page-header">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <h2>{sep_keyword11}</h2>
                    </div>
                    <div class="col-12">
                        <a href="/">홈</a>
                        <a href="/blog">Blog</a>
                        <a href="/blog/{sep_keyword0}">{sep_keyword11}</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="single">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="single-content wow fadeInUp">
                            <img src="../이미지/{image_url}" alt="{sep_keyword55}"/>
                            <h1>{sep_keyword11}</h1>
                            <img src="../이미지/{image_url2}" alt="{sep_keyword44}">
                            <p>
                                {sep_keyword11}배관이 PVC 재질이라면 너무 뜨거운 물을 사용하면 변형될 수 있으므로 70~80도 정도의 물을 사용하는 것이 좋다. 베이킹소다와 식초를 활용하는 방법도 있다. 베이킹소다는 지방을 분해하는 데 효과적이며, 식초와 만나면 거품을 발생시켜 {sep_keyword33} 해결하는 데 도움을 준다. 하수구에 베이킹소다 한 컵을 붓고 식초를 부으면 거품이 일어나면서 내부를 청소하는 효과가 있다. 약 1015분 정도 기다린 후 뜨거운 물을 부어주면 찌꺼기가 깨끗이 씻겨 내려간다. 이 방법은 화학 세제를 사용하지 않고도 하수구를 깨끗하게 관리할 수 있는 방법 중 하나다. {sep_keyword22}
                            </p>

                            <h2>{sep_keyword66}</h2>
                            <h3>{sep_keyword66} 잘 뚫는 곳</h3>
                            <img src="../이미지/{image_url3}" alt="{sep_keyword55}">
                            <p>
                                {sep_keyword11}하수구가 심하게 막혔다면 배관 청소 솔이나 배수구 클리너를 이용하여 직접 청소하는 것이 효과적이다. 특히 머리카락이 원인일 경우 배수구 트랩을 제거하고 고무장갑을 낀 후 손으로 제거하는 것이 가장 확실한 방법이다. 또한 플런저를 사용하면 압력을 이용해 {sep_keyword11} 막힌 부분을 뚫을 수 있다. 뚫어뻥을 사용할 때는 하수구에 약간의 물을 채운 상태에서 사용해야 효과가 좋다. 위아래로 여러 번 눌렀다 떼는 동작을 반복하면 압력 차이로 인해 막힌 부분이 뚫릴 수 있다. {sep_keyword33}
                            </p>
                            <img src="../이미지/{image_url4}" alt="{sep_keyword66}">
                            <img src="../이미지/{image_url5}" alt="{sep_keyword55}">
                            <h2>{sep_keyword55}</h2>
                            <h3>{sep_keyword55} 해결 전문업체</h3>
                            <p>
                                {sep_keyword11}배관이 심하게 노후화되었거나 내부에 단단한 이물질이 쌓인 경우일 수 있다. 이런 경우에는 전문가의 도움을 받아 고압 세척을 하거나 배관 교체를 고려해야 한다. 하수구가 자주 막히지 않도록 예방하는 것도 중요하다. 하수구 막힘을 해결하는 가장 기본적인 방법은 배수구 거름망을 사용하는 것이다. 머리카락이나 음식물 찌꺼기가 직접 배관으로 흘러 들어가는 것을 방지할 수 있어 주기적인 청소 부담을 줄일 수 있다. 주방에서는 기름기를 바로 하수구에 흘려보내지 않고 따로 처리하는 것이 좋으며, 욕실에서는 샴푸나 비누 찌꺼기가 쌓이지 않도록 물을 충분히 흘려 보내는 것이 도움이 된다. {sep_keyword77}
                                또한 한 달에 한두 번 정도 베이킹소다와 식초를 이용한 청소를 하면 하수구 내부의 찌꺼기를 예방할 수 있다. 하수구 막힘은 일상에서 불편을 초래하는 문제이지만, 원인을 파악하고 적절한 방법으로 {sep_keyword22} 해결하면 쉽게 극복할 수 있다. 무엇보다 중요한 것은 막히기 전에 미리 예방하는 것이다. 배수구 거름망 사용, 기름기 제거, 주기적인 청소 습관을 들이면 하수구가 막히는 일을 최소화할 수 있다. 만약 여러 가지 방법을 시도해도 해결되지 않는다면 전문가의 도움을 받아 배관 점검을 진행하는 것이 필요하다.{sep_keyword77}
                            </p>

                            <img src="../이미지/{image_url6}" alt="{sep_keyword44}">
                            <h2>{sep_keyword44}</h2>
                            <h3>{sep_keyword44} 24시 출동하는 업체</h3>
                            <p>
                                {sep_keyword11}하수구가 막히는 문제는 일상에서 흔히 겪는 불편한 상황 중 하나다. 특히 주방과 욕실에서 물이 원활하게 빠지지 않거나, 악취가 나는 경우에는 하수구 막힘이 원인일 가능성이 높다. 이를 해결하기 위해서는 먼저 막힘의 원인을 파악하는 것이 중요하다. {sep_keyword77} 하수구가 막히는 주된 원인은 머리카락, 음식물 찌꺼기, 기름때, 비누 찌꺼기, 배관 노후화 등이 있다. 욕실 하수구의 경우 머리를 감을 때 빠지는 머리카락이 배수구에 쌓이면서 물이 원활하게 내려가지 않는 경우가 많다. 여기에 비누 찌꺼기나 때가 엉겨 붙으면 더욱 심각한 막힘이 발생할 수 있다. 주방 하수구는 음식물 찌꺼기와 기름때가 주요 원인이다.{sep_keyword11}
                                <a href="https://seocho.the-drain.com">{sep_keyword66}</a>
                                특히 기름은 물과 만나면서 굳어지기 때문에 배수관 벽에 달라붙어 점점 더 두꺼운 막을 형성한다. 처음에는 물이 천천히 내려가다가 시간이 지나면서 완전히 막히는 경우도 발생한다. 이런 경우에는 평소에 기름을 하수구에 버리지 않고 키친타월 등으로 닦아내서 버리는 것이 예방하는 데 효과적이다. 하수구가 막혔을 때는 여러 가지 방법을 활용하여 {sep_keyword66} 해결할 수 있다. 가장 간단한 방법은 뜨거운 물을 붓는 것이다. 특히 기름이나 비누 찌꺼기 때문에 막힌 경우에는 뜨거운 물을 천천히 흘려보내면 배관에 붙어 있는 찌꺼기가 녹아내리면서 물이 잘 내려갈 수 있다.
                                {sep_keyword11}
                            </p>

                            <img src="../이미지/{image_url7}" alt="{sep_keyword55}">
                            <img src="../이미지/{image_url8}" alt="{sep_keyword66}">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <h2 style="text-align: center;">{sep_keyword66} 예방법</h2>
            <table>
                <thead>
                    <tr>
                        <th>문제</th>
                        <th>예방법</th>
                        <th>추가 팁</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{sep_keyword44}</td>
                        <td>{sep_keyword44} 생리대와 물티슈를 변기에 버리지 마세요.</td>
                        <td>화장지를 필요한 만큼만 사용하여 막힘을 방지하세요.</td>
                    </tr>
                    <tr>
                        <td>{sep_keyword55}</td>
                        <td>{sep_keyword55} 기름이나 기름기를 싱크대에 버리지 말고 종이타월로 닦아내세요.</td>
                        <td>거름망을 사용하여 음식물 찌꺼기가 배수구로 들어가지 않게 하세요.</td>
                    </tr>
                    <tr>
                        <td>{sep_keyword66}</td>
                        <td> {sep_keyword66}머리카락 필터를 설치하고 사용 후 정기적으로 청소하세요.</td>
                        <td>배수구에 뜨거운 물을 한 달에 한 번 부어 비누 찌꺼기를 제거하세요.</td>
                    </tr>
                </tbody>
            </table>

            <div class="faq-container ">
                <h2 class="wow fadeInUp">자주 묻는 질문</h2>
                <div class="accordion wow fadeInUp">
                    <div class="accordion-header">✅ {sep_keyword66} 해결 방법이 어떻게 되나요?</div>
                    <div class="accordion-body">기본장비부터 고가의 고압세척 장비와
        10년 이상의 전문가들로 빠르고 깔끔하게 하수구 막힘을 해결해드립니다.</div>
                </div>
                <div class="accordion wow fadeInUp">
                    <div class="accordion-header">✅ 24시 작업이 가능한가요?</div>
                    <div class="accordion-body">저희 더 드레인은 365일 24시 수도권 어디든 작업이 가능합니다. 👉🏼 1555-5492</div>
                </div>
                <div class="accordion wow fadeInUp">
                    <div class="accordion-header">✅ {sep_keyword44} 초기 대응 방법은 무엇인가요?</div>
                    <div class="accordion-body">뚜러뻥을 사용하거나 온수와 세제를 넣어 막힘을 완화시켜보세요.</div>
                </div>
                <div class="accordion wow fadeInUp">
                    <div class="accordion-header">✅ 변기막힘이 심할 경우 어떻게 해야 하나요?</div>
                    <div class="accordion-body">변기막힘 뚫는 전문업체에 연락하여 기계를 이용한 정밀한 처리를 받는 것이 좋습니다.</div>
                </div>
                <div class="accordion wow fadeInUp">
                    <div class="accordion-header">✅ 싱크대에서 물이 잘 내려가지 않아요. 원인은 무엇인가요?</div>
                    <div class="accordion-body">음식물 찌꺼기와 기름이 배수관에 쌓여 막힘을 유발했을 가능성이 높습니다.</div>
                </div>
            </div>



        <footer class="footer wow fadeIn" data-wow-delay="0.3s">
            <div style="text-align: left;">
                <h3 style="margin: 0;">{sep_keyword66}</h3>
                <p style="margin: 5px 0;">서초구하수구막힘, 싱크대막힘, 변기막힘 24시 전문 해결업체</p>
            </div>
            <div style="text-align: right;">
                <h4 style="margin-top: 10px;">연락처</h4>
                <p style="margin: 5px 0;">연락처: 1555-5492</p>
            </div>
        </footer>

        <a href="tel:1555-5492" class="call-button" title="전화하기">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/phone.png" alt="서초구하수구막힘">
        </a>  
        <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>
        <script src="../lib/easing/easing.min.js"></script>
        <script src="../lib/wow/wow.min.js"></script>
        <script src="../lib/owlcarousel/owl.carousel.min.js"></script>
        <script src="../lib/isotope/isotope.pkgd.min.js"></script>
        <script src="../lib/lightbox/js/lightbox.min.js"></script>
        <script src="../js/main.js"></script>
    </body>
</html>

"""



# 랜덤 색상 조정 함수
def random_color_adjustment(img):
    # 랜덤 밝기 조정
    brightness = random.uniform(0.5, 1.5)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)
    
    # 랜덤 대비 조정
    contrast = random.uniform(0.5, 1.5)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    
    # 랜덤 채도 조정
    saturation = random.uniform(0.5, 1.5)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(saturation)
    
    # 랜덤 색조 조정 (색상 이동)
    hue = random.uniform(-0.1, 0.1)
    img = img.convert("HSV")
    h, s, v = img.split()
    h = h.point(lambda p: (p + int(hue * 255)) % 255)
    img = Image.merge("HSV", (h, s, v)).convert("RGB")
    
    # 랜덤 필터 적용
    filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL, ImageFilter.SHARPEN]
    img = img.filter(random.choice(filters))
    
    return img
    
# 이미지를 다운로드하고 색 조정하기
def download_and_adjust_image(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        
        # 이미지 색 조정
        with Image.open(output_path) as img:
            # 예: 밝기 조정
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(random.uniform(0.5, 1.5))  # 밝기 조정


						# WebP 포맷으로 저장
            img.save(output_path, format='WEBP')

for index, url in enumerate(image_urls):
    output_path = os.path.join(temp_dir, f"{index}.webp")
    download_and_adjust_image(url, output_path)

# 랜덤으로 조정된 이미지 선택
adjusted_images = os.listdir(temp_dir)


# 출력 폴더 설정
output_folder = 'blog'
os.makedirs(output_folder, exist_ok=True)



def get_n_different_random_values(values_list, n):
    if len(values_list) < n:
        return values_list[:n]  # 값이 n개 미만일 경우 가능한 만큼 반환
    return random.sample(values_list, n)  # 서로 다른 n 개 값을 랜덤으로 선택




# 각 페이지마다 다른 이미지와 데이터를 넣어 HTML 파일 생성
for index, row in df.iterrows():

      # 랜덤 이미지 선택 (각 HTML 파일에 대해 새로 랜덤 이미지 선택)
    random_image_file = random.choice(adjusted_images)
    image_url = os.path.join(random_image_file)  # 랜덤 이미지 경로

    random_images = get_n_different_random_values(adjusted_images, 8)

    sep_keyword1 = row['Keyword']  # 엑셀의 'a' 열 데이터
    sep_keyword2 = row['Keyword2']  # 엑셀의 'b' 열 데이터
    sep_keyword3 = row['Keyword3']  # 엑셀의 'c' 열 데이터
    sep_keyword4 = row['Keyword4']  # 엑셀의 'd' 열 데이터
    sep_keyword5 = row['Keyword5']  # 엑셀의 'd' 열 데이터
    sep_keyword6 = row['Keyword6']  # 엑셀의 'd' 열 데이터
    sep_keyword7 = row['Keyword7']  # 엑셀의 'd' 열 데이터
    # sep_keyword8 = row['Keyword8']  # 엑셀의 'd' 열 데이터
    sep_keyword0 = row['Keyword'].replace(" ", "")

    
    # HTML 콘텐츠 생성
    html_content = html_template.format(
        sep_keyword11=sep_keyword1,
        sep_keyword22=sep_keyword2,
        sep_keyword33=sep_keyword3,
        sep_keyword44=sep_keyword4,
        sep_keyword55=sep_keyword5,
        sep_keyword66=sep_keyword6,
        sep_keyword77=sep_keyword7,
        # sep_keyword88=sep_keyword8,
        sep_keyword0=sep_keyword0,
        image_url=random_images[0],
        image_url2=random_images[1],
        image_url3=random_images[2],
        image_url4=random_images[3],
        image_url5=random_images[4],
        image_url6=random_images[5],
        image_url7=random_images[6],
        image_url8=random_images[7],
    )
    

    # 파일 이름 설정 (출력 폴더 경로 포함)
    file_name = os.path.join(output_folder, f"{sep_keyword0}.html")

    # HTML 파일로 저장
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)


print("HTML파일이 제작되었습니다.")