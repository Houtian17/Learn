package dome;

public class CD extends Item {
    private String artist;
    private int numofTracks;
    private int playingTime;
    private boolean gotIt = false;
    private String comment;

    public CD(String title, String artist, int numofTracks, int playingTime, String comment) {
        super(title, playingTime, false, comment);
        this.artist = artist;
        this.numofTracks = numofTracks;
//        this.playingTime = playingTime;
//        this.comment = comment;
    }

    public static void main(String[] args) {
        CD cd = new CD("1", "2", 3, 4, "d");
        cd.print();
    }


    @Override
    public boolean equals(Object obj) {
        CD cc = (CD) obj;
        return artist.equals(cc.artist);
    }

    @Override
    public void print() {
        System.out.println("CD:" + title + ":" + artist);
    }

}
