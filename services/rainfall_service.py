import xarray as xr


FILE_PATH = r"data\raw\RF25_ind2025_rfp25 (1).nc"


def get_rainfall_stats(latitude, longitude):
    ds = xr.open_dataset(FILE_PATH)

    rainfall = ds["RAINFALL"].sel(
        LATITUDE=latitude,
        LONGITUDE=longitude,
        method="nearest"
    )

    nearest_lat = float(rainfall.LATITUDE)
    nearest_lon = float(rainfall.LONGITUDE)

    values = rainfall.values

    print(f"Requested location : ({latitude}, {longitude})")
    print(f"Nearest IMD grid   : ({nearest_lat}, {nearest_lon})")

    print("\n=== Rainfall Statistics ===")
    print(f"Total rainfall : {float(values.sum()):.2f} mm")
    print(f"Average daily  : {float(values.mean()):.2f} mm")
    print(f"Maximum daily  : {float(values.max()):.2f} mm")
    print(f"Rainy days     : {int((values > 0).sum())}")

    print("\n=== Last 7 Days ===")
    print(rainfall.isel(TIME=slice(-7, None)).to_dataframe())

    ds.close()


if __name__ == "__main__":
    get_rainfall_stats(18.5204, 73.8567)