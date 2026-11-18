import pandas as pd
import plotly.express as px
import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="Employee Guidelines Page", page_icon="🍽", layout="wide")




# Security check
if not st.session_state.get("authenticated", False):
    st.switch_page("Main_Page.py")


def logout():

    st.session_state.authenticated = False
    st.switch_page("Main_Page.py")


# Sidebar
st.sidebar.image("MH_Logo1.png")
st.sidebar.title("Program Menu")

st.sidebar.page_link(
    "pages/01_NewFBReport.py",
    label="Enter New Report"
)

st.sidebar.page_link(
    "pages/02_FBReportSearch.py",
    label="Feedback Report Search"
)

st.sidebar.page_link(
    "pages/03_ReportDL.py",
    label="Feedback Report Download"
)

st.sidebar.page_link(
    "pages/04_GuidelinesPage.py",
    label="Guidelines Page"
)



if st.sidebar.button("Logout", type="tertiary"):
    logout()


#Program Proper
st.title("Mey Han Feedback Program")
st.header("Employee Guidelines Page")

@st.cache_resource
def init_supabase():
    url = st.secrets["supabase_URL"]
    key = st.secrets["supabase_Key"]
    return create_client (url, key)

supabase: Client = init_supabase()


with st.expander("**Catering Waiter Guidelines**", expanded=True):
    st.markdown("""
    **DESKRIPSYON NG TRABAHO (CHECKLIST)**
    - ☐ Tumulong sa head waiter at magsilbing onsite staff sa mga catering event.

    **MGA TUNGKULIN AT RESPONSIBILIDAD (CHECKLIST)**
    - ☐ Tumulong sa head waiter sa paghahanda bago ang event (pre-event preparation) ng mga kubyertos (utensils), kagamitan, at mantel (tablecloth).
    - ☐ Tumulong sa head waiter sa maayos na pagkakarga ng mga kubyertos, kagamitan, at mantel sa delivery truck.
    - ☐ Tumulong sa maayos na pagkakarga ng mga catering food sa delivery truck bago umalis (dispatch).
    - ☐ Tumulong sa maayos na pagbababa ng pagkain, kubyertos, kagamitan, at mantel pagdating sa venue.
    - ☐ Tumulong sa head waiter at sa mga kapwa catering waiter sa pag-setup bago ang event at sa paglilinis (cleanup) pagkatapos ng event.
    - ☐ Magbigay ng maayos at de-kalidad na serbisyo sa mga kliyente habang nagpapatuloy ang event.
    - ☐ Tumulong sa head waiter sa iba pang karagdagang pangangailangan sa serbisyo habang nagpapatuloy ang event.
    """)

    st.markdown("""
    ### MGA DAPAT AT HINDI DAPAT GAWIN SA EVENT (EVENT DOS AND DON'TS CHECKLIST)

    **SEKSYON 1: BAGO ANG EVENT (PRE-EVENT)**
    - ☐ **1.** TIYAKIN na kumpleto at nakahanda na ang lahat ng kubyertos, kagamitan, at mantel.
    - ☐ **2.** TIYAKIN na nakakarga na sa truck ang lahat ng kagamitang kailangan para sa event.
    - ☐ **3.** TIYAKIN na kumpleto at maayos na nakakarga sa delivery truck ang lahat ng catering food.

    **SEKSYON 2: HABANG NASA EVENT (EVENT PROPER)**
    - ☐ **1.** MAGSUOT nang maayos at presentable habang nagse-setup ng event (black shirt at black slacks).
    - ☐ **2.** TUMULONG sa head waiter upang matiyak na maayos ang pagkaka-setup ng venue at kumpleto sa kagamitan, kubyertos, at food warmers.
    - ☐ **3.** Kung may emergency, HUWAG aalis bago magsimula ang event nang hindi ipinapaalam sa management sa opisina at/o sa head waiter.
    - ☐ **4.** MAGSUOT nang maayos at presentable sa oras ng serbisyo (red uniform at black slacks).
    - ☐ **5.** HUWAG umalis sa event venue habang oras ng serbisyo.
    - ☐ **6.** SUNDIN ang lahat ng patakaran sa pagpasok (ingress) at regulasyon ng event venue.
    - ☐ **7.** HUWAG kumain o kumuha ng anumang catering food na inorder ng kliyente.
    - ☐ **8.** HUWAG uminom ng anumang alak o iba pang inumin kahit inalok pa ito ng kliyente.
    - ☐ **9.** HUWAG kumain ng anumang sobrang pagkain (extra food) na ibinigay ng kliyente.
    - ☐ **10.** HUWAG uminom ng tubig sa venue nang nakikita mismo ng mga bisita.
    - ☐ **11.** HUWAG kumain at/o magtabi ng anumang catering food o sobrang pagkain/inumin na dala ng kliyente.
    - ☐ **12.** HUWAG kumuha ng mga karagdagang photo o video ng event nang walang pahintulot.
    - ☐ **13.** TIYAKIN na maisisilbi nang maayos ang anumang karagdagang pagkain o inumin na ipapa-serve ng kliyente.
    - ☐ **14.** HUWAG mag-pack o magpabalot ng tirang pagkain (leftover food) nang walang paunang utos o pahintulot mula sa head waiter.
    - ☐ **15.** MAGBIGAY ng mahusay at de-kalidad na serbisyo sa buong oras ng event.
    - ☐ **16.** MAGTANONG sa head waiter o sa mga mas matagal nang catering waiter kung may anumang tanong o concern.

    **SEKSYON 3: PAGKATAPOS NG EVENT (POST-EVENT)**
    - ☐ **1.** SUNDIN ang mga patakaran at regulasyon ng venue sa paglabas (post-event egress).
    - ☐ **2.** TUMULONG sa head waiter upang matiyak na maayos na naimpake at naikarga sa delivery truck ang lahat ng kagamitan, kubyertos, at mantel.
    - ☐ **3.** TUMULONG sa head waiter upang matiyak na walang anumang gamit na naiwan sa venue.
    - ☐ **4.** Kung inutusan, MAGSAGAWA ng huling pag-check sa buong venue upang matiyak na walang naiwang gamit.
    - ☐ **5.** Kung may agarang concern o problema ang kliyente, TUMULONG sa head waiter (kung kinakailangan) sa pagkontak agad (ASAP) sa management sa opisina.
    - ☐ **6.** Kung may problema sa transportasyon, TUMULONG sa head waiter (kung kinakailangan) sa pagkontak agad (ASAP) sa management sa opisina.
    """)

with st.expander("**Catering Head Waiter Guidelines**", expanded=True):
    st.markdown("""
**DESKRIPSYON NG TRABAHO (CHECKLIST)**
- ☐ Magsilbing supervisor ng mga waiter sa mga onsite catering event.

**MGA TUNGKULIN AT RESPONSIBILIDAD (CHECKLIST)**
- ☐ Pamahalaan at subaybayan ang paghahanda bago ang event (pre-event preparation) ng mga kubyertos (utensils), kagamitan, at mantel (tablecloth).
- ☐ Subaybayan ang maayos na pagkakarga ng mga kubyertos, kagamitan, at mantel sa delivery truck.
- ☐ Subaybayan ang maayos na pagkakarga ng mga pagkain sa truck bago umalis (dispatch).
- ☐ Subaybayan ang maayos na pagbababa ng pagkain, kubyertos, kagamitan, at mantel pagdating sa venue.
- ☐ Pamahalaan ang mga catering waiter sa pag-setup bago ang event at sa paglilinis (cleanup) pagkatapos ng event.
- ☐ Subaybayan at pangasiwaan ang mga catering waiter bago, habang, at pagkatapos ng oras ng serbisyo.
- ☐ Magsilbing pangunahing tagapag-ugnay (onsite liaison) sa pagitan ng management sa opisina at ng kliyente habang nagpapatuloy ang event.
- ☐ Tiyakin na maibabalik sa opisina ang lahat ng kagamitan, kubyertos, at mantel na dinala sa venue.
- ☐ I-report sa opisina ang mga naging problema o feedback sa event, gaya ng komento ng kliyente, mga hiniram na kubyertos, aberya sa event, at iba pa.

### MGA DAPAT AT HINDI DAPAT GAWIN SA EVENT (EVENT DOS AND DON'TS CHECKLIST)

**SEKSYON 1: BAGO ANG EVENT (PRE-EVENT)**
- ☐ **1.** TIYAKIN na kumpleto at nakahanda na ang lahat ng kubyertos, kagamitan, at mantel.
- ☐ **2.** TIYAKIN na nakahanda na at nakakarga sa delivery truck ang lahat ng karagdagang request ng kliyente na nakalista sa production sheet.
- ☐ **3.** TIYAKIN na nakakarga na sa truck ang lahat ng kagamitang kailangan para sa event.
- ☐ **4.** TIYAKIN na kumpleto at maayos na nakakarga sa delivery truck ang lahat ng catering food.
- ☐ **5.** TIYAKIN na nakasakay na sa delivery truck ang lahat ng catering waiter.
- ☐ **6.** TIYAKIN na nakakarga na sa sasakyan ang mga personal na gamit ng lahat ng waiter bago umalis.
- ☐ **7.** TIYAKIN na may nakahandang maayos na pagkain o baon ang lahat ng waiter bago umalis.
- ☐ **8.** HUWAG ipaubaya sa mga catering waiter lang ang paghahanda bago ang event.
- ☐ **9.** HUWAG mag-iwan ng anumang catering food o iba pang karagdagang gamit para sa event.
- ☐ **10.** HUWAG umalis ng opisina hangga't hindi sigurado at pamilyar sa kumpletong address ng event venue.

**SEKSYON 2: HABANG NASA EVENT (EVENT PROPER)**
- ☐ **1.** TIYAKIN na maayos at presentable ang suot ng lahat ng catering waiter (black t-shirt + slacks) habang nagse-setup ng event.
- ☐ **2.** TIYAKIN na maayos ang pagkaka-setup ng venue at kumpleto sa kagamitan, kubyertos, food warmers, at staff.
- ☐ **3.** TIYAKIN na nasusunod at nagagawa ang mga karagdagang request ng kliyente habang nagse-setup ng venue.
- ☐ **4.** Kung may emergency, HUWAG aalis bago magsimula ang event nang hindi ipinapaalam sa management sa opisina at/o sa mga kasamahang catering waiter.
- ☐ **5.** TIYAKIN na ginagawa ng lahat ng catering staff ang kani-kanilang naka-assign na trabaho habang nagseserbisyo.
- ☐ **6.** TIYAKIN na maayos at presentable ang suot ng lahat ng kasamahang staff sa oras ng serbisyo (red uniform at black slacks).
- ☐ **7.** HUWAG umalis sa event venue habang oras ng serbisyo.
- ☐ **8.** TIYAKIN na nasusunod nang maayos ang lahat ng patakaran sa pagpasok (ingress) at regulasyon ng event venue.
- ☐ **9.** TIYAKIN na sumusunod ang lahat ng catering waiter sa mga patakaran at regulasyon ng event venue.
- ☐ **10.** TIYAKIN na naisisilbi ang lahat ng pagkaing inorder ng kliyente.
- ☐ **11.** HUWAG kumain o kumuha ng anumang catering food na inorder ng kliyente.
- ☐ **12.** HUWAG uminom ng anumang alak o iba pang inumin kahit inalok pa ito ng kliyente.
- ☐ **13.** HUWAG kumain ng anumang sobrang pagkain (extra food) na ibinigay ng kliyente.
- ☐ **14.** HUWAG uminom ng tubig sa venue nang nakikita mismo ng mga bisita.
- ☐ **15.** TIYAKIN na ang mga catering waiter ay HINDI umiinom ng tubig nang nakikita ng mga bisita.
- ☐ **16.** TIYAKIN na ang mga catering waiter ay HINDI kumakain at/o nagtatabi ng anumang catering food o extra food na dala ng kliyente.
- ☐ **17.** HUWAG kumuha ng mga karagdagang photo o video nang walang pahintulot, maliban kung para lang i-record o i-document ang setup ng event.
- ☐ **18.** TIYAKIN na maisisilbi nang maayos ang anumang karagdagang pagkain na ipapa-serve ng kliyente.
- ☐ **19.** HUWAG magpa-pack o magpabalot ng dagdag na pagkain nang walang paunang pahintulot mula sa kliyente.
- ☐ **20.** Kung may agarang pangangailangan sa event, IPAGBIGAY-ALAM agad (ASAP) sa management sa opisina.

**SEKSYON 3: PAGKATAPOS NG EVENT (POST-EVENT)**
- ☐ **1.** TIYAKIN na nasunod ang mga patakaran at regulasyon ng venue sa paglabas (post-event egress).
- ☐ **2.** TIYAKIN na maayos na naimpake at naikarga sa delivery truck ang lahat ng kagamitan, kubyertos, at mantel.
- ☐ **3.** TIYAKIN na walang anumang gamit na naiwan sa venue.
- ☐ **4.** Kung hihilingin ng kliyente na mag-iwan ng ilang gamit, GUMAWA ng kumpletong listahan at ipaalam agad sa opisina (ASAP).
- ☐ **5.** MAGSAGAWA ng huling pag-check sa buong venue upang matiyak na walang naiwang gamit bago umalis.
- ☐ **6.** Kung may agarang concern o problema ang kliyente, MAKIPAG-UGNAYAN AGAD sa management sa opisina.
- ☐ **7.** Kung may problema sa transportasyon, MAKIPAG-UGNAYAN AGAD sa management sa opisina para humingi ng tulong.
- ☐ **8.** Kung nagbayad ang kliyente sa venue (onsite), bago umalis ay I-SURRENDER agad ang cash o tseke sa driver at i-endorse ito agad sa management sa opisina.
""")


with st.expander("**Company Driver Guidelines**", expanded=True):
    st.markdown("""
**DESKRIPSYON NG TRABAHO (CHECKLIST)**
- ☐ Ligtas na pag-alis at nasa oras na pagdating sa tamang lokasyon ng lahat ng biyaheng naka-assign habang naka-duty.
- ☐ Mahigpit at legal na pagsunod sa batas at sa lahat ng patakaran sa trapiko habang naka-duty.
- ☐ Pangkalahatang pisikal at mekanikal na pagmamantina (maintenance) ng lahat ng sasakyang naka-assign.
- ☐ Paghahanda at pagkumpleto ng taunang rehistro (yearly registration) para sa lahat ng sasakyan.
- ☐ Pagtulong sa mga kasamahang staff sa pagkakarga at pagbababa ng mga gamit habang naka-duty.

**MGA TUNGKULIN AT RESPONSIBILIDAD (CHECKLIST)**
- ☐ Ligtas na pag-alis at nasa oras na pagdating sa tamang lokasyon ng lahat ng biyaheng naka-assign habang naka-duty.
- ☐ Mahigpit at legal na pagsunod sa batas at sa lahat ng patakaran sa trapiko habang naka-duty.
- ☐ Maayos na paghahanda upang matiyak na nasa oras ang pagdating sa biyahe, kasama ang pag-check ng tamang ruta papunta sa lokasyon para sa mga naka-assign na biyahe.
- ☐ Tiyakin na nasa maayos na kondisyon (good working condition) at handa nang bumiyahe ang sasakyan.
- ☐ Tiyakin na kumpleto ang sasakyan sa tamang mekanikal at dokumentaryong pangangailangan bago bumiyahe.
- ☐ Lingguhang pisikal na pagmamantina ng mga aktibong sasakyang ginagamit, kasama ang masusing paglilinis (deep clean) at mechanical check-up.
- ☐ Paghahanda at pagkumpleto ng taunang rehistro (yearly vehicle registration) para sa lahat ng sasakyan.
- ☐ Pagtulong sa mga kasamahang onsite staff (mga waiter / delivery person) sa pagkakarga at pagbababa ng mga gamit at pagkaing ide-deliver.
- ☐ Pagtulong sa pagbababa ng mga kagamitan pagkatapos ng biyahe o event, pati na rin sa paglilinis ng mga sasakyang ginamit.

**MGA PATAKARAN SA TRAFFIC FINES AT VIOLATIONS (CHECKLIST)**
- ☐ May ipinatutupad na two-strike system ang kumpanya para sa mga violation. Ang mga sumusunod ay ipapataw pagkatapos ng ikalawang paglabag (second offense).
- ☐ Ang mga violation at paglabag na dulot ng pagkakamali ng driver ay ibabawas sa sahod ng driver.
- ☐ Ang mga violation at paglabag na dulot lamang ng problema sa sasakyan ay sasagutin ng kumpanya.
- ☐ Ang mga violation at paglabag na dulot ng pinagsamang pagkakamali ng driver at problema sa sasakyan ay paghahatian ng kumpanya at ng driver.

**CHECKLIST NG MGA DAPAT I-REPORT SA OPERATIONS MANAGER**
- ☐ **1.** (Lingguhan) Estado o lagay ng mechanical at physical check-up para sa mga aktibong sasakyang ginagamit.
- ☐ **2.** (Kung Kinakailangan) Kasalukuyang mekanikal na lagay ng mga hindi aktibong sasakyan.
- ☐ **3.** (Kung Kinakailangan) Mga nawawala o kailangang repair tools para sa sasakyan.
- ☐ **4.** (Kung Kinakailangan) Nawawala o kailangang reserbang gulong (spare tire) ng sasakyan.
- ☐ **5.** (Taunan / Isang Buwan Bago ang Deadline) Mga paparating na deadline para sa rehistro ng sasakyan.
- ☐ **6.** (Buwanan / Dalawang Beses sa Isang Buwan) Lahat ng kailangang schedule sa maintenance ng sasakyan (gaya ng change oil, atbp.).
- ☐ **7.** (Kung Kinakailangan) Mga agaran (urgent) at hindi agarang (non-urgent) pagpapaayos na kailangan ng sasakyan.

### PRE-TRIP CHECKLIST (BAGO BUMIYAHE)

**SEKSYON 1: CHECKLIST SA KONDISYON NG SASAKYAN**
- ☐ **1.)** May sapat na gasolina ang sasakyan para sa buong biyahe.
- ☐ **2.)** Nakasakay na sa sasakyan ang reserbang gulong (spare tire) at mga repair tools.
- ☐ **3.)** Nasa maayos na kondisyon ang lahat ng gulong ng sasakyan.
- ☐ **4.)** Maayos na nag-o-on (umaandar) at nag-o-off (namamatay) ang sasakyan.
- ☐ **5.)** Walang problema sa baterya ang sasakyan.
- ☐ **6.)** Walang problema sa clutch, silinyador (acceleration), at preno (brake) ang sasakyan.
- ☐ **7.)** May sapat na tubig ang sasakyan para sa biyahe.

**SEKSYON 2: CHECKLIST SA BIYAHE**
- ☐ **1.)** Alam ng driver ang kumpletong address ng pupuntahan at may nakahanda nang ruta mula sa panggagalingang lokasyon.
- ☐ **2.)** Nakalagay sa glove compartment ng sasakyan ang pinakabagong (latest) OR/CR.
- ☐ **3.)** (Kung kinakailangan) May tamang toll fee trip cards (Autosweep/Easytrip) ang sasakyan na may load na para sa biyahe.
- ☐ **4.)** (Bago umalis) Nakakarga na sa sasakyan ang lahat ng kailangang gamit at items.
- ☐ **5.)** (Bago umalis) Nakasakay na sa sasakyan at handa nang umalis ang lahat ng onsite staff na naka-assign sa biyahe.

### CHECKLIST NG MGA PANG-ARAW-ARAW NA GAWAIN (DAILY TASK CHECKLIST)
- ☐ **1.)** Magtanong o i-check ang schedule para sa buong araw.
- ☐ **2.)** *Kung may naka-assign na biyahe:* I-check ang sasakyang gagamitin para sa naka-assign na biyahe.
- ☐ **3.)** Tiyakin na kumpleto ang sasakyan sa lahat ng kailangang mekanikal na gamit at dokumento para sa biyahe.
- ☐ **4.)** Tiyakin na nasa maayos na kondisyon (good working condition) at handa nang bumiyahe ang sasakyan.
- ☐ **5.)** I-check ang arrival address ng naka-assign na biyahe. Kung hindi pamilyar sa lugar, gumamit ng navigation apps (gaya ng Waze o Google Maps) para mahanap ang pinakamabilis at pinakamaayos na ruta.
- ☐ **6.)** *Kung walang naka-assign na biyahe:* I-check ang kasalukuyang mekanikal at pisikal na kondisyon ng mga aktibong sasakyan.
- ☐ **7.)** Kung kinakailangan, gawin ang pisikal na pagmamantina o paglilinis ng mga aktibong sasakyang ginagamit.

### MGA DAPAT AT HINDI DAPAT GAWIN SA BIYAHE AT PAGKATAPOS NG BIYAHE (TRIP & POST-TRIP DOS AND DON'TS)

**SEKSYON 1: HABANG NASA BIYAHE / ORAS NG EVENT (TRIP / SCHEDULE PROPER)**
- ☐ **1.** HUWAG labagin ang mga batas at patakaran sa trapiko habang naka-duty.
- ☐ **2.** HUWAG umalis sa venue dala ang sasakyan habang nagpapatuloy pa ang naka-assign na event.
- ☐ **3.** HUWAG mag-side trip o pumunta sa ibang lugar na walang kinalaman sa pangunahing biyaheng naka-assign.
- ☐ **4.** SUNDIN ang lahat ng patakaran at regulasyon ng mga venue o delivery location habang naka-duty.
- ☐ **5.** BUMALIK agad sa opisina pagkatapos makumpleto ang naka-assign na biyahe.
- ☐ **6.** MAKIPAG-UGNAYAN AGAD sa opisina kung may anumang problema o concern sa venue/onsite.

**SEKSYON 2: PAGKATAPOS NG BIYAHE (POST-TRIP)**
- ☐ **1.** I-SURRENDER ang lahat ng cash o check sales na ibinigay ng mga catering waiter pagkatapos ng bawat event.
- ☐ **2.** I-SURRENDER ang lahat ng sukli (cash change) mula sa mga binayarang parking, gate, o transport fee na ibinigay ng opisina.
- ☐ **3.** I-SURRENDER o i-report sa opisina ang lahat ng posibleng gamit na naiwan sa venue ayon sa hiling ng kliyente (kung kinakailangan).
- ☐ **4.** TUMULONG sa pagbababa ng mga kagamitan o items na natira sa sasakyan pagdating sa opisina.
- ☐ **5.** LINISIN ang sasakyan pagkatapos ng delivery o event (post-use vehicle cleanup).
""")
