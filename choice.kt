import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.view.View
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.Response
import com.android.volley.toolbox.JsonObjectRequest
import com.android.volley.toolbox.Volley
import org.json.JSONObject

class MainActivity : AppCompatActivity() {

    private lateinit var requestQueue: RequestQueue

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        requestQueue = Volley.newRequestQueue(this)
    }

    fun onOptionButtonClick(view: View) {
        val option: String
        val question: String

        // 선택지와 질문 설정
        when (view.id) {
            //1
            R.id.buttonOption1 -> {
                option = "차나 오토바이로 자유로운 여행을 즐기는 것"
                question = "여행할  때 선호하는 교통 수단은 무엇인가요?"
            }
            R.id.buttonOption2 -> {
                option = "공공 교통을 이용해 현지인들과 함께 이동하는 것"
                question = "여행할  때 선호하는 교통 수단은 무엇인가요?"
            }
            R.id.buttonOption3 -> {
                option = "비행기로 멀리 떠나는 것"
                question = "여행할  때 선호하는 교통 수단은 무엇인가요?"
            }
            R.id.buttonOption4 -> {
                option = "자전거로 체력을 쑥쑥 키우는 것"
                question = "여행할  때 선호하는 교통 수단은 무엇인가요?"
            }
            //2
            R.id.buttonOption1 -> {
                option = "신나는 파티나 축제에 참여하는 것"
                question = "여행할 때 나는 어떤 종류의 경험을 선호하나요?"
            }
            R.id.buttonOption2 -> {
                option = "조용한 휴식과 자연을 즐기는 것"
                question = "여행할 때 나는 어떤 종류의 경험을 선호하나요?"
            }
            R.id.buttonOption3 -> {
                option = "유적지나 역사적 장소를 탐험하는 것"
                question = "여행할 때 나는 어떤 종류의 경험을 선호하나요?"
            }
            R.id.buttonOption4 -> {
                option = "새로운 문화와 인종을 경험하는 것"
                question = "여행할 때 나는 어떤 종류의 경험을 선호하나요?"
            }
            //3
            R.id.buttonOption1 -> {
                option = "현지 먹거리와 음식 문화를 체험하는 것"
                question = "여행 중 나는 어떤 종류의 음식을 선호하나요?"
            }
            R.id.buttonOption2 -> {
                option = "미리 알고 있는 음식을 먹는 것"
                question = "여행 중 나는 어떤 종류의 음식을 선호하나요?"
            }
            R.id.buttonOption3 -> {
                option = "특별한 식사 경험 (미술관 내 레스토랑, 뷔페 등)"
                question = "여행 중 나는 어떤 종류의 음식을 선호하나요?"
            }
            R.id.buttonOption4 -> {
                option = "빠른 식사 (패스트푸드, 패스트캐주얼 등)"
                question = "여행 중 나는 어떤 종류의 음식을 선호하나요?"
            }
            //4
            R.id.buttonOption1 -> {
                option = "자연과 풍경의 아름다움"
                question = "여행지를 선택할 때 가장 중요한 것은 무엇인가요?"
            }
            R.id.buttonOption2 -> {
                option = "역사와 문화의 깊이 있는 경험"
                question = "여행지를 선택할 때 가장 중요한 것은 무엇인가요?"
            }
            R.id.buttonOption3 -> {
                option = "먹거리와 음식 문화의 다양성"
                question = "여행지를 선택할 때 가장 중요한 것은 무엇인가요?"
            }
            R.id.buttonOption4 -> {
                option = ""
                question = "여행지를 선택할 때 가장 중요한 것은 무엇인가요?"
            }
            //5
            R.id.buttonOption1 -> {
                option = "봄의 꽃길을 걷으며 청량한 공기를 마시는 것"
                question = "여행을 할 때 가장 선호하는 계절은 무엇인가요?"
            }
            R.id.buttonOption2 -> {
                option = "여름 바다에서 해수욕을 즐기고 캠핑을 하는 것"
                question = "여행을 할 때 가장 선호하는 계절은 무엇인가요?"
            }
            R.id.buttonOption3 -> {
                option = "가을의 단풍구경과 포근한 온천을 즐기는 것"
                question = "여행을 할 때 가장 선호하는 계절은 무엇인가요?"
            }
            R.id.buttonOption4 -> {
                option = "겨울의 스키장에서 눈썰매를 타는 것"
                question = "여행을 할 때 가장 선호하는 계절은 무엇인가요?"
            }
            //6
            R.id.buttonOption1 -> {
                option = "숙박 시설의 가격과 품질을 중점적으로 고려하는 것"
                question = "여행지를 선택할 때 어떤 것을 가장 고려하나요?"
            }
            R.id.buttonOption2 -> {
                option = "대중교통이 발달되어 있어 이동이 편리한 것"
                question = "여행지를 선택할 때 어떤 것을 가장 고려하나요?"
            }
            R.id.buttonOption3 -> {
                option = "유명한 명소나 특별한 이벤트가 있는 곳을 선택하는 것"
                question = "여행지를 선택할 때 어떤 것을 가장 고려하나요?"
            }
            R.id.buttonOption4 -> {
                option = "현지의 문화와 역사를 체험하며 지식과 경험을 쌓는 것"
                question = "여행지를 선택할 때 어떤 것을 가장 고려하나요?"
            }
            //7
            R.id.buttonOption1 -> {
                option = "호텔이나 리조트와 같은 고급스러운 숙박 시설을 선호하는 것"
                question = "여행할 때 선호하는 숙박 시설은 무엇인가요?"
            }
            R.id.buttonOption2 -> {
                option = "로컬 펜션과 같은 복잡한 분위기의 숙박 시설을 선호하는 것"
                question = "여행할 때 선호하는 숙박 시설은 무엇인가요?"
            }
            R.id.buttonOption3 -> {
                option = "에어비앤비와 같은 로컬 렌탈 하우스를 선호하는 것"
                question = "여행할 때 선호하는 숙박 시설은 무엇인가요?"
            }
            R.id.buttonOption4 -> {
                option = "캠핑이나 카라반 같은 아웃도어 숙박 시설을 선호하는 것"
                question = "여행할 때 선호하는 숙박 시설은 무엇인가요?"
            }
            //8
            R.id.buttonOption1 -> {
                option = "야외 활동(예: 트레킹, 등산, 서핑 등)"
                question = "여행중에 가장 좋아하는 활동은?"
            }
            R.id.buttonOption2 -> {
                option = "문화 관광(예: 박물관, 유적지, 사원, 궁전 등)"
                question = "여행중에 가장 좋아하는 활동은?"
            }
            R.id.buttonOption3 -> {
                option = "쇼핑 및 시장 탐방"
                question = "여행중에 가장 좋아하는 활동은?"
            }
            R.id.buttonOption4 -> {
                option = "공연 및 축제 참가"
                question = "여행중에 가장 좋아하는 활동은?"
            }
            //9
            R.id.buttonOption1 -> {
                option = "스트레스 해소와 휴식을 취하기 위해서"
                question = "여행을 떠나는 목적은 무엇인가요?"
            }
            R.id.buttonOption2 -> {
                option = "새로운 경험과 문화, 사람들을 만나기 위해서"
                question = "여행을 떠나는 목적은 무엇인가요?"
            }
            R.id.buttonOption3 -> {
                option = "여행을 통해 세상을 보며 배우기 위해서"
                question = "여행을 떠나는 목적은 무엇인가요?"
            }
            R.id.buttonOption4 -> {
                option = "자연과 문화를 경험하며 감동과 충만한 추억을 쌓기 위해서"
                question = "여행을 떠나는 목적은 무엇인가요?"
            }
            //10
            R.id.buttonOption1 -> {
                option = "자유여행"
                question = "여행을 할 때 선호하는 방식은 무엇인가요?"
            }
            R.id.buttonOption2 -> {
                option = "패키지 여행"
                question = "여행을 할 때 선호하는 방식은 무엇인가요?"
            }
            R.id.buttonOption3 -> {
                option = "단체 여행"
                question = "여행을 할 때 선호하는 방식은 무엇인가요?"
            }
            R.id.buttonOption4 -> {
                option = "배낭 여행"
                question = "여행을 할 때 선호하는 방식은 무엇인가요?"
            }
            //11
            R.id.buttonOption1 -> {
                option = "여행 중 얻는 지식과 경험의 깊이"
                question = "여행을 할 때 가장 중요하게 고려하는 것은 무엇인가요?"
            }
            R.id.buttonOption2 -> {
                option = "여행 목적지의 다양한 관광지와 놀거리"
                question = "여행을 할 때 가장 중요하게 고려하는 것은 무엇인가요?"
            }
            R.id.buttonOption3 -> {
                option = "여행 중 인생샷과 사진을 남기는 것"
                question = "여행을 할 때 가장 중요하게 고려하는 것은 무엇인가요?"
            }
            R.id.buttonOption4 -> {
                option = "여행 기간 동안의 휴식과 여유"
                question = "여행을 할 때 가장 중요하게 고려하는 것은 무엇인가요?"
            }
            //12
            R.id.buttonOption1 -> {
                option = "여행 가이드북"
                question = "여행을 할 때 어떤 종류의 책을 가지고 가고 싶나요?"
            }
            R.id.buttonOption2 -> {
                option = "소설"
                question = "여행을 할 때 어떤 종류의 책을 가지고 가고 싶나요?"
            }
            R.id.buttonOption3 -> {
                option = "자기계발서"
                question = "여행을 할 때 어떤 종류의 책을 가지고 가고 싶나요?"
            }
            R.id.buttonOption4 -> {
                option = "만화책"
                question = "여행을 할 때 어떤 종류의 책을 가지고 가고 싶나요?"
            }
            //13
            R.id.buttonOption1 -> {
                option = "특산품 및 기념품"
                question = "여행을 할 때 어떤 종류의 쇼핑을 선호하시나요?"
            }
            R.id.buttonOption2 -> {
                option = "유명 브랜드의 쇼핑몰"
                question = "여행을 할 때 어떤 종류의 쇼핑을 선호하시나요?"
            }
            R.id.buttonOption3 -> {
                option = "지역 시장 및 벼룩시장"
                question = "여행을 할 때 어떤 종류의 쇼핑을 선호하시나요?"
            }
            R.id.buttonOption4 -> {
                option = "수공예품 및 공예체험"
                question = "여행을 할 때 어떤 종류의 쇼핑을 선호하시나요?"
            }
        }

        // 선택지와 질문을 서버로 전송
        val url = "http://your-server-url/save_option"
        val params = JSONObject()
        params.put("option", option)
        params.put("question", question)

        val jsonObjectRequest = JsonObjectRequest(Request.Method.POST, url, params,
            Response.Listener { response ->
                // 서버로부터의 응답 처리
                // ...
            },
            Response.ErrorListener { error ->
                // 에러 처리
                // ...
            })

        requestQueue.add(jsonObjectRequest)
    }
}