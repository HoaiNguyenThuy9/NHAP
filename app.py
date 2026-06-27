import streamlit as st

# ==============================================================================
# ĐỊNH CẤU HÌNH TRANG & CSS NÂNG CAO (CHUẨN UI/UX FINTECH NGÂN HÀNG)
# ==============================================================================
st.set_page_config(page_title="APP CHO VAY ONLINE KHCN - THUY HOAI", layout="wide")

st.markdown("""
    <style>
    /* Nền trang và màu chữ chủ đạo mềm mại */
    .stApp {
        background-color: #f4f7f6;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Thiết kế Banner đỉnh trang */
    .banking-hero {
        background: linear-gradient(135deg, #0a4d3c 0%, #1f8266 100%);
        color: white;
        padding: 40px 50px;
        border-radius: 24px;
        margin-bottom: 35px;
        box-shadow: 0 10px 30px rgba(10, 77, 60, 0.15);
    }
    
    /* Khối Hộp (Card) Chứa các Phân Đoạn */
    .ui-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        border: none;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .ui-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.07);
    }
    
    /* Tiêu đề phân đoạn với điểm nhấn màu xanh */
    .ui-headline {
        color: #0a4d3c;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 25px;
        padding-left: 12px;
        border-left: 5px solid #1f8266;
    }
    
    /* Thiết kế lại các widget nhập liệu của Streamlit cho hiện đại */
    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stNumberInput input {
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: #f8fafc !important;
        padding: 4px 12px !important;
        color: #334155 !important;
    }
    
    /* Nút bấm Đăng ký phong cách bo góc, đổ bóng (Glow Button) */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #0a4d3c 0%, #1f8266 100%);
        color: white !important;
        border: none;
        padding: 16px 40px;
        font-size: 1.2rem;
        font-weight: 700;
        border-radius: 14px;
        box-shadow: 0 10px 25px rgba(31, 130, 102, 0.3);
        width: 100%;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        margin-top: 15px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #063328 0%, #155b47 100%);
        box-shadow: 0 12px 30px rgba(31, 130, 102, 0.5);
        transform: scale(1.01);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# THANH SIDEBAR
# ==============================================================================
# Sử dụng link ảnh icon online để phòng trường hợp file "tài chính.png" của bạn bị lỗi đường dẫn
URL_LOGO = "https://cdn-icons-png.flaticon.com/512/2830/2830284.png"
st.sidebar.image(URL_LOGO, width=100)
st.sidebar.markdown("<h3 style='color:#0a4d3c; margin-top:10px;'>HỆ THỐNG TÍN DỤNG</h3>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.info("🏢 **Đơn vị thẩm định:** NHÓM 6\n\nHệ thống phê duyệt tự động giảm thời gian xử lý hồ sơ xuống còn 3 giây.")

# ==============================================================================
# BANNER TIÊU ĐỀ ỨNG DỤNG
# ==============================================================================
st.markdown("""
    <div class="banking-hero">
        <h1 style="margin:0; font-size: 2.4rem; font-weight: 800; letter-spacing: -0.5px;">🏦 ĐĂNG KÝ VÀ KIỂM TRA ĐIỀU KIỆN VAY VỐN</h1>
        <p style="margin: 12px 0 0 0; opacity: 0.9; font-size: 1.1rem; font-weight: 300;">
            Hệ thống tự động chấm điểm tín dụng và tính toán dòng tiền chi trả trực tuyến của Khách hàng.
        </p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# PHẦN 1: ĐỊNH DANH (Bọc trong Hộp giao diện UI)
# ==============================================================================
st.markdown('<div class="ui-card">', unsafe_allow_html=True)
st.markdown('<div class="ui-headline">🪪 1. Xác thực thông tin định danh cá nhân</div>', unsafe_allow_html=True)

col_id1, col_id2, col_id3 = st.columns([1.5, 1.5, 2])
with col_id1:
    ho_ten = st.text_input("Họ và tên chủ hồ sơ:", value="Nguyễn Văn A")
with col_id2:
    cccd = st.text_input("Số Căn cước công dân (12 số):", value="012345678901")
with col_id3:
    dia_chi = st.text_input("Địa chỉ cư trú hiện tại:", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")

st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN 2 & 3: HAI KHỐI NHẬP LIỆU SONG SONG (LAYOUT GRID CÂN BẰNG)
# ==============================================================================
col_grid1, col_grid2 = st.columns(2)

with col_grid1:
    st.markdown('<div class="ui-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="ui-headline">📋 2. Nhu cầu phân kỳ vay vốn</div>', unsafe_allow_html=True)
    
    loai_vay = st.selectbox(
        "Hình thức cấp tín dụng muốn đăng ký:", 
        ["Vay tiêu dùng tín chấp (Không cần tài sản)", "Vay mua Ô tô (Thế chấp bằng xe)", "Vay mua Bất động sản (Thế chấp bằng đất/nhà)", "Vay sản xuất kinh doanh"]
    )
    muc_dich = st.text_input("Mục đích sử dụng số tiền cụ thể:", value="Mua nhà chung cư / Chi tiêu gia đình")
    
    STV = st.number_input("Số tiền muốn đề xuất vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian hoàn trả mong muốn (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất tạm tính (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    
    if "Không cần tài sản" in loai_vay:
        GTTSDB = 0.0
        st.caption("ℹ️ Hệ thống miễn kê khai tài sản bảo đảm đối với hình thức vay Tín chấp.")
    else:
        GTTSDB = st.number_input("Ước tính giá trị Tài sản thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)
    
    hinh_thuc_tra = st.selectbox(
        "Phương thức trả nợ định kỳ:", 
        ["Gốc đều, lãi giảm dần (Kỳ đầu cao nhất, giảm dần về sau)", "Gốc và lãi chia đều cố định hàng tháng (Annuity)"]
    )
    nguon_chinh = st.selectbox(
        "Nguồn thu nhập chính dùng để trả nợ:", 
        ["Lương từ công việc cố định (Có HĐLĐ)", "Thu nhập từ hộ kinh doanh / Doanh nghiệp riêng", "Thu nhập từ việc cho thuê tài sản (Nhà, xe)", "Thu nhập tự do không cố định"]
    )
    nguon_phu = st.selectbox(
        "Nguồn thu nhập bổ sung hỗ trợ:", 
        ["Không có", "Thu nhập bổ sung từ Vợ/Chồng", "Tiền gửi tiết kiệm / Tài sản tích lũy khác"]
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_grid2:
    st.markdown('<div class="ui-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="ui-headline">👤 3. Thông tin năng lực tài chính & Lịch sử CIC</div>', unsafe_allow_html=True)
    
    STKH = st.number_input("Số tuổi hiện tại của bạn:", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân hiện nay:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    
    nghe_nghiep_mapping = {
        "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
        "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
        "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
        "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
    }
    nghe_chon = st.selectbox("Công việc/Nghề nghiệp hiện tại:", list(nghe_nghiep_mapping.keys()))
    nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
    
    TN = st.number_input("Tổng thu nhập bình quân tháng (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người phụ thuộc tài chính trong gia đình:", min_value=0, value=1, step=1)
    PTMC = st.number_input("Số tiền đang phải trả gốc lãi nơi khác hằng tháng (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("<p style='margin-top:15px; margin-bottom:5px; font-weight:
