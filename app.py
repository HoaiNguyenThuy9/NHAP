import streamlit as st

# ==============================================================================
# CẤU HÌNH TRANG WEB & THEME THEO PHONG CÁCH VIETCOMBANK
# ==============================================================================
st.set_page_config(page_title="Personal Loans - Vietcombank Style", layout="wide")

# CSS tạo dựng layout phẳng, bo góc nhỏ nhẹ, nút tinh tế và màu xanh Vietcombank (#00a651)
st.markdown("""
    <style>
    /* Nền tổng thể tinh giản trắng/xám mịn */
    .stApp {
        background-color: #fafafa;
        font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Thanh điều hướng giả định phía trên */
    .vcb-nav-sub {
        background-color: #ffffff;
        padding: 12px 20px;
        border-bottom: 1px solid #e1e4e6;
        margin-bottom: 25px;
        border-radius: 8px;
    }
    .vcb-nav-sub span {
        color: #78828a;
        font-size: 0.9rem;
    }
    .vcb-nav-sub strong {
        color: #00a651;
        font-size: 0.9rem;
    }

    /* Tiêu đề trang */
    .vcb-main-title {
        color: #1c2430;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .vcb-sub-title {
        color: #78828a;
        font-size: 1.05rem;
        margin-bottom: 30px;
    }
    
    /* Thiết kế thẻ Card trắng chuẩn Vietcombank */
    .vcb-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 0px; 
        margin-bottom: 25px;
        border: 1px solid #eef0f2;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
        overflow: hidden;
    }
    
    /* Phần chứa nội dung padding phía dưới ảnh */
    .vcb-card-body {
        padding: 25px;
    }
    
    /* Tiêu đề trong mỗi Card dịch vụ */
    .vcb-card-header {
        color: #1c2430;
        font-size: 1.25rem;
        font-weight: 600;
        border-left: 4px solid #00a651;
        padding-left: 12px;
        margin-bottom: 20px;
    }
    
    /* Định hình lại các ô nhập liệu Streamlit phẳng và thanh mảnh */
    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stNumberInput input {
        border-radius: 6px !important;
        border: 1px solid #dcdfe3 !important;
        background-color: #ffffff !important;
        color: #1c2430 !important;
    }
    
    /* Nút bấm Đăng ký Vay màu xanh lục Vietcombank */
    div.stButton > button:first-child {
        background-color: #00a651;
        color: #ffffff !important;
        border: none;
        padding: 14px 30px;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 6px;
        width: 100%;
        transition: background-color 0.2s ease;
        margin-top: 10px;
    }
    div.stButton > button:first-child:hover {
        background-color: #008741;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar thương hiệu
st.sidebar.markdown("<h2 style='color:#00a651; font-weight:800; text-align:center;'>Vietcombank</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#78828a; font-size:0.85rem;'>Chung niềm tin, vững tương lai</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.info("🏢 **Đơn vị phát triển:** NHÓM 6\n\nHệ thống thẩm định dòng tiền tự động dành cho Khách hàng cá nhân.")

# ==============================================================================
# THANH BREADCRUMB (ĐIỀU HƯỚNG PHỤ TRÊN WEBSITE)
# ==============================================================================
st.markdown("""
    <div class="vcb-nav-sub">
        <span>Trang chủ / Khách hàng cá nhân / Sản phẩm dịch vụ / </span><strong>Vay vốn trực tuyến</strong>
    </div>
""", unsafe_allow_html=True)

# BANNER TRÊN CÙNG: Sử dụng ảnh phong cảnh cây cầu (KHCN_MB NGANG_Dark.webp)
try:
    st.image("KHCN_MB NGANG_Dark.webp", use_container_width=True)
except:
    st.warning("⚠️ Không tìm thấy file 'KHCN_MB NGANG_Dark.webp' trong thư mục.")

st.markdown('<h1 class="vcb-main-title" style="margin-top:20px;">Gói Vay Vốn Khách Hàng Cá Nhân</h1>', unsafe_allow_html=True)
st.markdown('<p class="vcb-sub-title">Vietcombank đồng hành cùng bạn hiện thực hóa các kế hoạch tiêu dùng, mua nhà, mua xe và sản xuất kinh doanh.</p>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN 1: ĐỊNH DANH (Sử dụng ảnh Ava_NHA MOI THANH DAT_DT.webp làm cover)
# ==============================================================================
st.markdown('<div class="vcb-card">', unsafe_allow_html=True)
try:
    st.image("Ava_NHA MOI THANH DAT_DT.webp", use_container_width=True)
except:
    pass

st.markdown("""
        <div class="vcb-card-body">
            <div class="vcb-card-header">Thông tin khách hàng đăng ký đơn vay</div>
""", unsafe_allow_html=True)

col_id1, col_id2, col_id3 = st.columns([1.5, 1.5, 2])
with col_id1:
    ho_ten = st.text_input("Họ và tên khách hàng:", value="Nguyễn Văn A")
with col_id2:
    cccd = st.text_input("Số CCCD (12 chữ số):", value="012345678901")
with col_id3:
    dia_chi = st.text_input("Địa chỉ cư trú hiện tại (Tỉnh/TP, Quận/Huyện...):", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")

st.markdown('</div></div>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN 2 & 3: BỐ CỤC SONG SONG (GRID SYSTEM) CÓ HÌNH ẢNH RIÊNG
# ==============================================================================
col_grid1, col_grid2 = st.columns(2)

with col_grid1:
    # Cột nhu cầu vay: Sử dụng ảnh gia đình trước nhà (ChoVayTinDungTieuDung_mb.jpg)
    st.markdown('<div class="vcb-card" style="height: 100%;">', unsafe_allow_html=True)
    try:
        st.image("ChoVayTinDungTieuDung_mb.jpg", use_container_width=True)
    except:
        pass
        
    st.markdown("""
            <div class="vcb-card-body">
                <div class="vcb-card-header">Chi tiết nhu cầu vay vốn</div>
    """, unsafe_allow_html=True)
    
    danh_sach_loai_vay = [
        "Vay tiêu dùng tín chấp (Không cần tài sản)", 
        "Vay mua Ô tô (Thế chấp bằng xe)", 
        "Vay mua Bất động sản (Thế chấp bằng đất/nhà)", 
        "Vay sản xuất kinh doanh"
    ]
    loai_vay = st.selectbox("Sản phẩm cho vay mong muốn:", danh_sach_loai_vay)
    muc_dich = st.text_input("Mục đích sử dụng nguồn vốn giải ngân:", value="Mua nhà chung cư / Chi tiêu gia đình")
    
    STV = st.number_input("Số tiền đề xuất vay vốn (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian đăng ký hoàn trả (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất tạm tính (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    
    if "Không cần tài sản" in loai_vay:
        GTTSDB = 0.0
        st.caption("ℹ️ Gói vay tiêu dùng tín chấp không yêu cầu giá trị tài sản bảo đảm.")
    else:
        GTTSDB = st.number_input("Giá trị ước tính của Tài sản thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)
    
    danh_sach_tra = [
        "Gốc đều, lãi giảm dần (Kỳ đầu cao nhất, giảm dần về sau)", 
        "Gốc và lãi chia đều cố định hàng tháng (Annuity)"
    ]
    hinh_thuc_tra = st.selectbox("Phương thức trả nợ gốc và lãi hằng kỳ:", danh_sach_tra)
    
    danh_sach_nguon_chinh = [
        "Lương từ công việc cố định (Có HĐLĐ)", 
        "Thu nhập từ hộ kinh doanh / Doanh nghiệp riêng", 
        "Thu nhập từ việc cho thuê tài sản (Nhà, xe)", 
        "Thu nhập tự do không cố định"
    ]
    nguon_chinh = st.selectbox("Nguồn thu nhập chính chi trả nợ gốc:", danh_sach_nguon_chinh)
    
    danh_sach_nguon_phu = [
        "Không có", 
        "Thu nhập bổ sung từ Vợ/Chồng", 
        "Tiền gửi tiết kiệm / Tài sản tích lũy khác"
    ]
    nguon_phu = st.selectbox("Nguồn thu nhập tích lũy dự phòng:", danh_sach_nguon_phu)
    st.markdown('</div></div>', unsafe_allow_html=True)

with col_grid2:
    # Cột tài chính & CIC: Sử dụng ảnh nam thanh niên mặc áo len xanh (1 (1).webp)
    st.markdown('<div class="vcb-card" style="height: 100%;">', unsafe_allow_html=True)
    try:
        st.image("1 (1).webp", use_container_width=True)
    except:
        pass
        
    st.markdown("""
            <div class="vcb-card-body">
                <div class="vcb-card-header">Năng lực tài chính & Lịch sử tín dụng</div>
    """, unsafe_allow_html=True)
    
    STKH = st.number_input("Số tuổi hiện tại của chủ đơn:", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân dân sự:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    
    nghe_nghiep_mapping = {
        "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
        "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
        "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
        "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
    }
    nghe_chon = st.selectbox("Phân loại nhóm công việc/nghề nghiệp:", list(nghe_nghiep_mapping.keys()))
    nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
    
    TN = st.number_input("Tổng mức thu nhập hằng tháng (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người đang phụ thuộc kinh tế trực tiếp:", min_value=0, value=1, step=1)
    PTMC = st.number_input("Số tiền đang trả nợ định kỳ ở các TCTD khác (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("""
        <p style="margin-top:15px; margin-bottom:5px; font-weight:600; color:#1c2430;">Báo cáo quan hệ tín dụng cũ:</p>
    """, unsafe_allow_html=True)
    
    danh_sach_no_cu =
