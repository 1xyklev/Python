class Playlist:
    def __init__(self, name):
        self.tracks = []
        self.name = name
    
    def add(self, track):
        self.tracks.append(track)

    def count(self):
        print(len(self.tracks))

    def show(self):
        return f"플리명: {self.name}, 곡 수: {len(self.tracks)}, 곡들: [{','.join(self.tracks)}]"     # join을 써서 리스트 안의 요소들 묶기

pl = Playlist("MyList")
pl.add("Dynamite")
pl.add("Butter")
print(pl.show())    # 플리명: MyList, 곡 수: 2, 곡들: [Dynamite, Butter]