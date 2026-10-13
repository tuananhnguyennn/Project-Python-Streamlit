import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dữ liệu gốc và xử lý (Giống Colab)
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [8.0, 9.0, 7.0, 10.0, 6.0, 8.0, 9.0, 5.0, 10.0, 7.0],
    'Giữa kỳ': [7.5, 8.0, 6.5, 9.0, 5.5, 7.0, 8.5, 4.5, 9.5, 6.0],
    'Cuối kỳ': [8.0, 8.5, 7.0, 9.5, 6.0, 7.5, 9.0, 5.0, 9.0, 6.5]
}
df = pd.DataFrame(data)
df['Tổng kết'] = 0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'
df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# 2. Xây dựng giao diện Streamlit
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.header("1. Bảng điểm chi tiết")
st.dataframe(df, use_container_width=True)

st.header("2. Thống kê chung")
diem_tb = df['Tổng kết'].mean()
sv_cao = df[df['Tổng kết'] == df['Tổng kết'].max()].iloc[0]
sv_thap = df[df['Tổng kết'] == df['Tổng kết'].min()].iloc[0]
so_sv_dat = len(df[df['Tổng kết'] >= 5.0])

# Dùng cột để hiển thị thống kê đẹp hơn
col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm TB lớp", f"{diem_tb:.2f}")
col2.metric("Cao nhất", f"{sv_cao['Họ và tên']} ({sv_cao['Tổng kết']})")
col3.metric("Thấp nhất", f"{sv_thap['Họ và tên']} ({sv_thap['Tổng kết']})")
col4.metric("Số SV Đạt", so_sv_dat)

st.header("3. Tra cứu thông tin cá nhân")
# Tạo dropdown menu
selected = st.selectbox("Chọn tên sinh viên để xem chi tiết:", df['Họ và tên'])
# Lấy dữ liệu của sinh viên được chọn
thong_tin = df[df['Họ và tên'] == selected].iloc[0]

c1, c2, c3 = st.columns(3)
c1.info(f"**Chuyên cần:** {thong_tin['Chuyên cần']}")
c2.info(f"**Giữa kỳ:** {thong_tin['Giữa kỳ']}")
c3.info(f"**Cuối kỳ:** {thong_tin['Cuối kỳ']}")
st.success(f"🔥 **Điểm tổng kết:** {thong_tin['Tổng kết']:.2f} | **Xếp loại:** {thong_tin['Xếp loại']}")

st.header("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Họ và tên'], df['Tổng kết'], color='#3498db')
ax.set_title('Điểm tổng kết của 10 sinh viên')
ax.set_xlabel('Họ và tên')
ax.set_ylabel('Điểm tổng kết')
ax.set_ylim(0, 10)
for i, v in enumerate(df['Tổng kết']):
    ax.text(i, v + 0.2, f"{v:.1f}", ha='center')
st.pyplot(fig) # Lệnh in biểu đồ ra web

st.markdown("---")
# ĐỪNG QUÊN THAY ĐỔI DÒNG NÀY THÀNH TÊN CỦA BẠN
st.markdown("<p style='text-align: center; font-size: 14px; color: gray;'>Họ tên: Nguyễn Văn A - MSSV: 12345678</p>", unsafe_allow_html=True)