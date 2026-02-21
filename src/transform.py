import pandas as pd

def decode_series_key(series_key, series_dims):
  """
  Given a series key and its dimensions e.g. 29:0:0:0:0:8:0:0. decode each part into a
  dictionary mapping each dimension into a human-readable name.
  """
  indices = series_key.split(":")
  decoded = {}
  for i, idx in enumerate(indices):
      position = int(idx)
      dim_def = series_dims[i]
      # Each dimension's values is a list of dictionaries containing an
      # 'id' and a 'name' (the human-readable label)
      decoded[dim_def["id"]] = dim_def["values"][position]["name"]

  return decoded

def parse_oecd_cpi(json_data):
  structures = json_data["data"]["structures"]

  # First structure object contains our dimensions
  structure = structures[0]
  series_dims = structure["dimensions"]["series"]

  # Get the dataset
  dataSets = json_data["data"]["dataSets"]

  # The series object holds all the observations keyed by composite keys
  series_data = dataSets[0].get("series", {})

  records = []
  for key, info in series_data.items():
    # Decode the composite key into dimension values
    decoded = decode_series_key(key, series_dims)

    # Determine the country
    country = decoded.get("LOCATION")
    if not country:
      country = list(decoded.values())[0]

    # For each observations/records in the series get the inflation value
    observations = info.get("observations", {})
    for obs_index, obs_value in observations.items():
      # The first element in the obs_value list is the inflation rate
      inflation = obs_value[0]
      records.append({
          "Country": country,
          "ObservationIndex": obs_index,
          "Inflation (%)": inflation,
      })

  return pd.DataFrame(records)