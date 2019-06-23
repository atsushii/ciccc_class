/**
 *
 */
package assignment2;

import java.util.ArrayList;

/**
 * @author miyamotoatsushi
 *  implement assignment
 */
public class Holiday {

    private String name;
    private int day;
    String month;

    /**
     * constructor
     * @param name
     * @param day
     * @param month
     */
    public Holiday(String name, int day, String month) {
        this.name = name;
        this.day = day;
        this.month = month;
    }

    /**
     * calculate avarage
     * @param dayArray having day data
     * @return day avarage
     */
    public static double avgDate(ArrayList<Holiday> dayArray) {
        int sum = 0;
        for (Holiday a : dayArray) {
            sum += a.day;
        }
        return sum / dayArray.size();

    }

}
