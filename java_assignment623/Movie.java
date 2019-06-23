/**
 *
 */
package assignment2;

import java.util.ArrayList;

/**
 * @author miyamotoatsushi
 * implement assignment
 */
public class Movie {

    private String title;
    private String studio;
    private String rating;

    /**
     * constructor
     * @param title
     * @param studio
     * @param rating
     */
    public Movie(String title, String studio, String rating) {
        this.title = title;
        this.studio = studio;
        this.rating = rating;
    }

    /**
     * constructor
     * @param title
     * @param studio
     */
    public Movie(String title, String studio) {
        this.title = title;
        this.studio = studio;
        this.rating = "PG";
    }

    /**
     * create new array which is filtering rete of PG
     * @param movieList
     * @return new array which is filtering rete of PG
     */
    public static ArrayList<Movie> getPG(ArrayList<Movie> movieList) {
        ArrayList<Movie> newMovieList = new ArrayList<Movie>();
        for (Movie a : movieList) {
            if ("PG" == a.rating) {
                newMovieList.add(a);
            }
        }
        return newMovieList;

    }

}
