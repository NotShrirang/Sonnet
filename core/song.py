import streamlit as st

class Song:
    def __init__(self, name, artist) -> None:
        self.name = name
        self.artist = artist
        self.album_art = "https://tse1.mm.bing.net/th?q=" + name + " " + artist + "album art image"
        self.link = "https://www.google.com/search?q=" + name + " " + artist


def show_songs(results):
    col1, col2 = st.columns(2)
    for i in range(4):
        col = col1 if i % 2 == 0 else col2
        song = Song(results[i].metadata['song'], results[i].metadata['artist'])
        col.image(song.album_art, width=200)
        col.write("Song: " + song.name)
        col.write("Artist: " + song.artist)
        col.link_button("Listen", song.link)
        with col.expander("Lyrics"):
            st.subheader("Lyrics:")
            lyrics = results[i].page_content
            lyrics = lyrics.replace("  ", "\n")
            st.write(lyrics)