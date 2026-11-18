import xarray as xr

FILE_PATH = r"data\raw\RF25_ind2025_rfp25 (1).nc"

ds = xr.open_dataset(FILE_PATH)

rainfall = ds["RAINFALL"]

print("=== Rainfall Dataset ===")
print(f"Days       : {rainfall.sizes['TIME']}")
print(f"Latitudes  : {rainfall.sizes['LATITUDE']}")
print(f"Longitudes : {rainfall.sizes['LONGITUDE']}")

print("\n=== Geographic Range ===")
print(f"Latitude  : {float(ds.LATITUDE.min())} to {float(ds.LATITUDE.max())}")
print(f"Longitude : {float(ds.LONGITUDE.min())} to {float(ds.LONGITUDE.max())}")

print("\n=== Rainfall ===")
print(f"Unit : {rainfall.attrs['units']}")
print(f"Min  : {float(rainfall.min())} mm")
print(f"Max  : {float(rainfall.max())} mm")

ds.close()