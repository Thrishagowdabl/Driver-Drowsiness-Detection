import os
import shutil
import random

# ✅ Paths (make sure Open and Closed folders are in same directory as this script)
SOURCE_OPEN = "Open_Eyes"
SOURCE_CLOSED = "Closed_Eyes"

DEST_TRAIN_OPEN = "dataset/train/open"
DEST_TEST_OPEN = "dataset/test/open"
DEST_TRAIN_CLOSED = "dataset/train/closed"
DEST_TEST_CLOSED = "dataset/test/closed"

# ✅ Create required folders if not present
for path in [DEST_TRAIN_OPEN, DEST_TEST_OPEN, DEST_TRAIN_CLOSED, DEST_TEST_CLOSED]:
    os.makedirs(path, exist_ok=True)

def split_data(source, train_dir, test_dir, split_ratio=0.8):
    if not os.path.exists(source):
        print(f"❌ Source folder not found: {source}")
        return
    
    files = [f for f in os.listdir(source) if f.lower().endswith(('.jpg','.jpeg','.png','.bmp'))]

    if len(files) == 0:
        print(f"⚠ No images found in {source}")
        return

    random.shuffle(files)
    split_index = int(len(files) * split_ratio)

    train_files = files[:split_index]
    test_files = files[split_index:]

    print(f"\n📂 Splitting: {source}")
    print(f"➡ Train: {len(train_files)} images → {train_dir}")
    print(f"➡ Test:  {len(test_files)} images → {test_dir}")

    for file in train_files:
        shutil.copy(os.path.join(source, file), train_dir)

    for file in test_files:
        shutil.copy(os.path.join(source, file), test_dir)

# ✅ Perform split
split_data(SOURCE_OPEN, DEST_TRAIN_OPEN, DEST_TEST_OPEN)
split_data(SOURCE_CLOSED, DEST_TRAIN_CLOSED, DEST_TEST_CLOSED)

print("\n✅ ALL DONE!")
print("✔ Images successfully divided into TRAIN and TEST folders.")
