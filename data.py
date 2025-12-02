## Alternatif Code Label Encoding dengan menyimpan mappingnya

# print("\n=== DIMENSIONALITY REDUCTION: LABEL ENCODING ===")

# df_dim = df_reduced.copy()   # df_reduced = data setelah drop email

# label_cols = ["Name", "Gender", "City", "Department"]

# encoders = {}
# for col in label_cols:
#     le = LabelEncoder()
#     df_dim[col] = le.fit_transform(df_dim[col])
#     encoders[col] = le
#     # print(f"\nMapping {col}: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# print("\n=== DATASET SETELAH DIMENSIONALITY REDUCTION ===")
# print(df_dim)
