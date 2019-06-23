/**
 *
 */
package assignment2;

import java.util.ArrayList;

/**
 * @author miyamotoatsushi
 *  implement each classes
 */
public class ApplicationDrive {

    /**
     * implement each methods
     */
    public static void main(String[] args) {
        implementHoliday();
        System.out.println(inSameMonth());

        implementMovie();
    }

    /**
     * compare to month
     * @return true if month is equal and false they not
     */
    public static boolean inSameMonth() {
        Holiday holiday = new Holiday("aaa", 4, "July");
        Holiday holiday2 = new Holiday("bbb", 5, "August");

        if (holiday.month == holiday2.month) {
            return true;
        }
        return false;

    }

    /**
     * implement avgDate which is calculate avarage number from array
     */
    public static void implementHoliday() {
        Holiday holiday = new Holiday("Independence Day", 4, "July");
        ArrayList<Holiday> dayArray = new ArrayList<Holiday>();
        dayArray.add(holiday);
        dayArray.add(holiday);
        dayArray.add(holiday);
        System.out.println(holiday.avgDate(dayArray));

    }

    /**
     * implement getPG method which is creat new array
     */
    public static void implementMovie() {
        ArrayList<Movie> movieArray = new ArrayList<Movie>();

        Movie movie = new Movie("Casino Royale", "Eon Productions", "PG-13");
        Movie movie1 = new Movie("aaaaaaaaa", "aaaa", "PG-14");
        Movie movie2 = new Movie("bbbbbb", "bbbb", "PG");
        movieArray.add(movie);
        movieArray.add(movie1);
        movieArray.add(movie2);
        movieArray.add(movie);

        System.out.println(movie.getPG(movieArray));

    }



}
