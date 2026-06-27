import streamlit as st

# -----------------------------------------------------------------------------
# CẤU HÌNH TRANG & GIAO DIỆN SANG TRỌNG (CUSTOM CSS)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Hệ Thống Tài Chính Cao Cấp - Premium Finance", 
    page_icon="👑", 
    layout="wide"
)

# Nhúng CSS để đổi màu chủ đạo sang Vàng Champagne, Trắng Ngọc Trai và Xanh Than
st.markdown("""
    <style>
    /* Đổi font chữ toàn trang thành font thanh lịch */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Montserrat', sans-serif;
        background-color: #FAFAFA; /* Trắng ngọc trai */
        color: #1A2530; /* Chữ màu xanh than đậm */
    }
    
    /* Tùy biến tiêu đề lớn phong cách Luxury */
    .luxury-title {
        font-family: 'Playfair Display', serif;
        color: #C5A059; /* Vàng Champagne */
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }
    .luxury-subtitle {
        text-align: center;
        font-style: italic;
        color: #5A6B7C;
        margin-bottom: 40px;
    }
    
    /* Phong cách hóa các khối sản phẩm (Cards) */
    .product-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #C5A059; /* Viền vàng mảnh bên trái */
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        height: 250px;
    }
    .product-title {
        font-family: 'Playfair Display', serif;
        color: #1A2530;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    /* Khối kết quả tính tiền */
    .result-box {
        background-color: #F4EFE3; /* Nền kem nhạt */
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #E6D8B8;
        text-align: center;
        margin-top: 15px;
    }
    .result-amount {
        color: #C5A059;
        font-size: 1.8rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HEADER (THANH ĐIỀU HƯỚNG)
# -----------------------------------------------------------------------------
col_logo, col_menu = st.columns([1, 2])
with col_logo:
    st.markdown("<h2 style='color: #C5A059; margin: 0; font-family: \"Playfair Display\";'>👑 PRIME FINANCE</h2>", unsafe_allow_html=True)
with col_menu:
    st.markdown("<p style='text-align: right; padding-top: 10px; color: #5A6B7C;'>Hotline Đặc Quyền: 1800-8888 (24/7)</p>", unsafe_allow_html=True)

st.write("---")

# TIÊU ĐỀ CHÍNH
st.markdown("<div class='luxury-title'>GIẢI PHÁP TÀI CHÍNH XỨNG TẦM VỊ THẾ</div>", unsafe_allow_html=True)
st.markdown("<div class='luxury-subtitle'>Bảo mật - Tối ưu - Kiến tạo đặc quyền cá nhân dành riêng cho bạn</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# THÂN TRANG: CHIA LÀM 2 CỘT (CÔNG CỤ TÍNH VÀ FORM ĐĂNG KÝ)
# -----------------------------------------------------------------------------
col_calc, col_form = st.columns([1.2, 1])

with col_calc:
    st.markdown("<h3 style='font-family: \"Playfair Display\"; color: #1A2530;'>⚜️ Công Cụ Tính Khoản Vay Ưu Đãi</h3>", unsafe_allow_html=True)
    st.caption("Kéo chọn hạn mức và thời gian để ước tính số tiền cần trả hàng tháng.")
    
    # Các thanh trượt chọn số tiền và thời gian
    so_tien_vay = st.slider("Số tiền bạn cần vay (VND)", min_value=50000000, max_value=2000000000, value=200000000, step=50000000, format="%d")
    thoi_gian_vay = st.slider("Thời hạn vay (Tháng)", min_value=12, max_value=60, value=24, step=6)
    
    # Giả định lãi suất cố định là 8.5% một năm (0.7% một tháng) để tính toán nhanh
    lai_suat_nam = 8.5 / 100
    lai_suat_thang = lai_suat_nam / 12
    
    # Công thức tính trả góp đều hàng tháng (Thành phần gốc + lãi)
    goc_va_lai = (so_tien_vay * lai_suat_thang * (1 + lai_suat_thang)**thoi_gian_vay) / ((1 + lai_suat_thang)**thoi_gian_vay - 1)
    
    # Hiển thị kết quả tính toán
    st.markdown(f"""
        <div class="result-box">
            <p style="margin: 0; color: #5A6B7C; font-size: 0.9rem;">Số tiền ước tính trả góp hàng tháng</p>
            <p class="result-amount">{goc_va_lai:,.0f} VND</p>
            <p style="margin: 0; color: #8A9AAB; font-size: 0.8rem;">*Ước tính dựa trên lãi suất ưu đãi hiện hành {lai_suat_nam*100}%/năm</p>
        </div>
    """, unsafe_allow_html=True)

with col_form:
    st.markdown("<h3 style='font-family: \"Playfair Display\"; color: #1A2530;'>⚜️ Đăng Ký Tư Vấn Đặc Quyền</h3>", unsafe_allow_html=True)
    
    # Form nhận thông tin từ khách hàng
    with st.form("loan_registration_form", clear_on_submit=True):
        ho_ten = st.text_input("Họ và tên khách hàng *")
        so_dien_thoai = st.text_input("Số điện thoại liên hệ *")
        goi_vay_quan_tam = st.selectbox("Gói dịch vụ bạn quan tâm", [
            "Vay Tín Chấp Đặc Quyền (Personal Loan)",
            "Tài Trợ Sở Hữu Xe Sang (Auto Financing)",
            "Giải Pháp Bất Động Sản An Cư (Home Loan)"
        ])
        ghi_chu = st.text_area("Yêu cầu riêng biệt (nếu có)", placeholder="Ví dụ: Giờ gọi điện tiện nhất...")
        
        # Nút submit được thiết kế lại
        submit_btn = st.form_submit_button("GỬI YÊU CẦU ĐĂNG KÝ")
        
        if submit_btn:
            if ho_ten and so_dien_thoai:
                st.success(f"Xin cảm ơn ông/bà **{ho_ten}**. Chuyên viên cấp cao của Prime Finance sẽ liên hệ lại qua số {so_dien_thoai} trong vòng 15 phút.")
                # Ở đây bạn có thể viết thêm code kết nối Database để lưu data khách hàng.
            else:
                st.error("Vui lòng điền đầy đủ Họ tên và Số điện thoại để chúng tôi hỗ trợ.")

st.write("---")

# -----------------------------------------------------------------------------
# CÁC GÓI SẢN PHẨM (PRODUCT CARDS)
# -----------------------------------------------------------------------------
st.markdown("<h3 style='font-family: \"Playfair Display\"; text-align: center; color: #1A2530; margin-bottom: 25px;'>Danh Mục Giải Pháp Tài Chính</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="product-card">
            <div class="product-title">👑 Vay Tín Chấp Đặc Quyền</div>
            <p style="font-size: 0.9rem; color: #5A6B7C;">Hạn mức tối đa lên tới 1 Tỷ đồng không cần tài sản thế chấp. Thủ tục bảo mật, giải ngân siêu tốc trong 24 giờ làm việc.</p>
            <p style="font-size: 0.85rem; color: #C5A059; font-weight: bold;">Lãi suất từ: 7.9% / năm</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="product-card">
            <div class="product-title">🏎️ Tài Trợ Sở Hữu Xe Sang</div>
            <p style="font-size: 0.9rem; color: #5A6B7C;">Hỗ trợ tới 85% giá trị xe, thời gian vay linh hoạt tới 7 năm. Liên kết trực tiếp với các hãng xe hạng sang toàn quốc.</p>
            <p style="font-size: 0.85rem; color: #C5A059; font-weight: bold;">Lãi suất từ: 6.8% / năm</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="product-card">
            <div class="product-title">🏛️ Bất Động Sản An Cư</div>
            <p style="font-size: 0.9rem; color: #5A6B7C;">Giải pháp sở hữu căn hộ cao cấp hoặc biệt thự nghỉ dưỡng. Hạn mức vay không giới hạn dựa trên tài sản đảm bảo.</p>
            <p style="font-size: 0.85rem; color: #C5A059; font-weight: bold;">Lãi suất từ: 5.5% / năm</p>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.write("---")
st.markdown("<p style='text-align: center; color: #8A9AAB; font-size: 0.8rem;'>© 2026 Prime Finance. Mọi quyền được bảo lưu. Bản quyền giao diện thuộc về định hướng Premium UI.</p>", unsafe_allow_html=True)
