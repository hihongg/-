import random
deck = [
    ("A ♥", "Phở"), ("A ♦", "Cơm tấm"), ("A ♣", "Bánh mì"), ("A ♠", "Bún đậu mắm tôm"),
    ("2 ♥", "Bún bò Huế"), ("2 ♦", "Cơm gà"), ("2 ♣", "Bánh xèo"), ("2 ♠", "Bún chả"),
    ("3 ♥", "Bún riêu"), ("3 ♦", "Cơm sườn"), ("3 ♣", "Bánh cuốn"), ("3 ♠", "Nem nướng"),
    ("4 ♥", "Hủ tiếu"), ("4 ♦", "Cơm chiên"), ("4 ♣", "Bánh khọt"), ("4 ♠", "Gỏi cuốn"),
    ("5 ♥", "Miến gà"), ("5 ♦", "Cơm bò lúc lắc"), ("5 ♣", "Bánh căn"), ("5 ♠", "Chả giò"),
    ("6 ♥", "Cháo sườn"), ("6 ♦", "Cơm niêu"), ("6 ♣", "Bánh ướt"), ("6 ♠", "Ốc các loại"),
    ("7 ♥", "Bánh canh"), ("7 ♦", "Cơm cá kho"), ("7 ♣", "Bánh bèo"), ("7 ♠", "Lẩu Thái"),
    ("8 ♥", "Bún mọc"), ("8 ♦", "Cơm gà xối mỡ"), ("8 ♣", "Bánh đúc"), ("8 ♠", "Lẩu bò"),
    ("9 ♥", "Bún thang"), ("9 ♦", "Cơm trộn"), ("9 ♣", "Bánh hỏi"), ("9 ♠", "Lẩu hải sản"),
    ("10 ♥", "Mì Quảng"), ("10 ♦", "Cơm chay"), ("10 ♣", "Bánh tráng nướng"), ("10 ♠", "BBQ nướng"),
    ("J ♥", "Bún cá"), ("J ♦", "Cơm cà ri"), ("J ♣", "Bánh tráng trộn"), ("J ♠", "Gà nướng"),
    ("Q ♥", "Bún chả cá"), ("Q ♦", "Cơm vịt"), ("Q ♣", "Bánh bột lọc"), ("Q ♠", "Vịt quay"),
    ("K ♥", "Bún mắm"), ("K ♦", "Cơm thịt kho"), ("K ♣", "Bánh bao"), ("K ♠", "Hải sản")
]
n = int(input("Nhập số lần rút món: "))
if n > len(deck):
    print("Không thể rút quá 52 món")
else:
    picks = random.sample(deck, n)
    print("\n🍽️ Các món được chọn:")
    for i, (card, food) in enumerate(picks, 1):
        print(f"{i}. {card} → {food}")