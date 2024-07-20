def get_channel_sections_videos(channel_id, api_service_name="youtube"):
  """Fetches the first 4 videos from each section (playlist) of a YouTube channel.

  Args:
      channel_id: The ID of the YouTube channel.
      api_service_name: The name of the YouTube Data API service (default: "youtube").

  Returns:
      A dictionary where keys are section titles and values are lists of video IDs.
  """

  # Replace with your API key from the JSON key file
  api_key = "YOUR_API_KEY"

  youtube = googleapiclient.discovery.build(
      api_service_name, "v3", developerKey=api_key)

  # Get playlists associated with the channel
  playlists_list_request = youtube.playlists().list(
      part="snippet",
      channelId=channel_id,
      maxResults=50
  )
  response = playlists_list_request.execute()

  sections_videos = {}
  for playlist in response["items"]:
    playlist_title = playlist["snippet"]["title"]
    sections_videos[playlist_title] = []

    # Get videos within the playlist (section)
    playlist_items_list_request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist["id"],
        maxResults=4  # Get only the first 4 videos
    )
    playlist_items_response = playlist_items_list_request.execute()

    for video_item in playlist_items_response.get("items", []):
      video_id = video_item["snippet"]["resourceId"]["videoId"]
      sections_videos[playlist_title].append(video_id)

  return sections_videos

if __name__ == "__main__":
  # Replace with the channel ID you want to scrape
  channel_id = "@PW-Foundation"
  sections_with_videos = get_channel_sections_videos("@PW-Foundation")
  print(sections_with_videos)
