from src.api_extract import *
from src.data_cleaning import *
from src.visualization import *
from src.report_generator import *

channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"

# Get uploads playlist
playlist_id = get_uploads_playlist_id(
    channel_id
)

# Get video ids
video_ids = get_video_ids(
    playlist_id
)

# Get video details
df = get_video_details(video_ids)

# Clean data
df = clean_data(df)

# Generate graphs
generate_graphs(df)

# Generate report
create_report(df)

#Generate Coorelation png
correlation_heatmap(df)

#CSV file saved
save_csv(df)

print("Project Completed Successfully")