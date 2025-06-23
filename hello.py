from playwright.sync_api import sync_playwright
import time


def open_browser():

    print("브라우저를 열고있어요")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        page = browser.new_page()
        page.goto("https://www.google.com")
        print("브라우저가 열림")
        print("10초후 닫힘")

        time.sleep(10)

        browser.close()
        print("닫힘")

def go_to_naver_map():
    print("네이버 지도로 이동해요")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        page = browser.new_page()
        page.goto("https://map.naver.com")
        print("브라우저가 열림")
        print("10초후 닫힘")

        time.sleep(10)

        browser.close()
        print("닫힘")

def search_naver_map():
    print("네이버 지도로 이동해요")

    search_word = input("어떤 맛집 찾아줄까")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        page = browser.new_page()
        search_url = f"https://map.naver.com/p/search/{search_word}"
        page.goto(search_url)
        print(f"{search_word}이동")
        print("로딩")
        time.sleep(10)
        print("결과 확인")
        time.sleep(20)

        browser.close()
        print("닫힘")

def explore_page_data():
    """페이지 데이터 탐색하기"""
    
    print("네이버 지도 페이지의 데이터를 탐색해봐요!")
    
    search_word = input("어떤 맛집을 찾을까요? (예: 강남역 맛집): ")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        # 검색 페이지로 이동
        search_url = f"https://map.naver.com/p/search/{search_word}"
        page.goto(search_url)
        print(f"'{search_word}' 검색 페이지로 이동!")
        
        # 페이지 로딩 대기
        time.sleep(10)
        
        print("\n=== 페이지 데이터 분석 시작! ===")
        
        # 1. 페이지 제목 확인
        title = page.title()
        print(f"📄 페이지 제목: {title}")
        
        # 2. 현재 URL 확인
        current_url = page.url
        print(f"🔗 현재 URL: {current_url}")
        
        # 3. li 요소가 몇 개 있는지 확인
        li_elements = page.locator("li").all()
        print(f"📋 페이지에서 찾은 li 요소 개수: {len(li_elements)}개")
        
        # 4. div 요소가 몇 개 있는지 확인  
        div_elements = page.locator("div").all()
        print(f"📦 페이지에서 찾은 div 요소 개수: {len(div_elements)}개")
        
        # 5. iframe이 있는지 확인
        iframe_elements = page.locator("iframe").all()
        print(f"🖼️ 페이지에서 찾은 iframe 개수: {len(iframe_elements)}개")
        
        if len(iframe_elements) > 0:
            print("   ✅ iframe을 발견했어요! 맛집 정보가 이 안에 있을 수 있어요.")
            
            # iframe의 id 확인
            for i, iframe in enumerate(iframe_elements):
                iframe_id = iframe.get_attribute("id")
                iframe_src = iframe.get_attribute("src")
                
                # iframe_id가 None이면 "없음"으로 표시
                if iframe_id is None:
                    iframe_id = "없음"
                
                # iframe_src가 None이면 "없음"으로 표시
                if iframe_src is None:
                    iframe_src = "없음"
                else:
                    # src가 너무 길면 앞 50글자만 보여주기
                    iframe_src = iframe_src[:50] + "..." if len(iframe_src) > 50 else iframe_src
                
                print(f"   iframe {i+1}: id='{iframe_id}', src='{iframe_src}'")
        
        print("\n=== 30초 동안 페이지를 자세히 관찰해보세요! ===")
        print("💡 F12를 눌러서 개발자 도구도 열어보세요!")
        time.sleep(30)
        
        browser.close()
        print("🔚 데이터 탐색 완료!")

if __name__ == "__main__":
    search_naver_map()