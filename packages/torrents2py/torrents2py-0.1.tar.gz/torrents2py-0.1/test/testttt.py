from torrents2py import search_torrents

# Perform a search without filters
results, magnet_links = search_torrents("Insert search")
print(results)

# The search_torrents function returns a tuple with two elements:
# - results: a list of dictionaries, each containing information about a torrent,
#            including Title, Uploaded, Size, Seeds, Peers, etc.
# - magnet_links: a list of magnet links corresponding to each torrent in the results.

# Print all the torrents info that has been found
print("\nSearch Results:")
for index, result in enumerate(results, start=1):
    print(f"\nTorrent {index} Information:\n"
            f"   Title:    {result['Title']}\n"
            f"   Uploaded: {result['Uploaded']}" + " ago\n"
            f"   Size:     {result['Size']}\n"
            f"   Seeds:    {result['Seeds']}\n"
            f"   Peers:    {result['Peers']}\n"
            f"   Magnet Link: {magnet_links[index - 1]}\n")
