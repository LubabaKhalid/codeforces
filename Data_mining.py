from sklearn.datasets import fetch_openml
boston = fetch_openml(name="boston", as_frame=True)
df = boston.frame
