import java.util.*;
import java.text.SimpleDateFormat;

public class TestReservation
{
    static String datePattern = "MMM dd, yyyy";
    static SimpleDateFormat dateFormat = new SimpleDateFormat(datePattern);
    static Map<String, Integer> roomTypes = new HashMap<>() {{
        put("RoomWBath", 200);
        put("RoomWView", 175);
        put("NormalRoom", 120);
    }};

    static public void main(String[] args) 
    {
        executeTests(1, "RoomWBath", "Jan 02, 2025", "Jan 05, 2025");
    }

    static public void executeTests(int custId, String roomType, String startDate, String endDate) {
        System.out.println("Testing Reservation " + custId);
        System.out.printf("Arguments: %d, %s, %s, %s\n", custId, roomType, startDate, endDate);
        System.out.println("------------------------------");
        Reservation reservation = new Reservation(custId, roomType, startDate, endDate);
        testConstruction(reservation);
        testUUID(reservation);
        testReservationDate(reservation);
        testGuestID(reservation);
    }

    static public long calculateReservationNumberOfDays(Reservation reservation) {
        long numberOfDays = 0;
        try {
            Date startDate = dateFormat.parse(reservation.getReservationStartDate());
            Date endDate = dateFormat.parse(reservation.getReservationEndDate());
            //                                                         864000000
            numberOfDays = (endDate.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24);
        } catch (Exception e) {
            e.printStackTrace();
        }

        return numberOfDays;
    }

    static public int areDatesSimilar(Date d1, Date d2) {
        Calendar cal1 = Calendar.getInstance();
        cal1.setTime(d1);
        Calendar cal2 = Calendar.getInstance();
        cal2.setTime(d2);
        return (cal1.get(Calendar.YEAR) == cal2.get(Calendar.YEAR) &&
                cal1.get(Calendar.MONTH) == cal2.get(Calendar.MONTH) &&
                cal1.get(Calendar.DAY_OF_MONTH) == cal2.get(Calendar.DAY_OF_MONTH)) ? 1 : 0;

    }

    static public void testConstruction(Reservation reservation) {
        System.out.println("Construction Tests");
        Assert.assertEqualsInt(1, reservation.getGuestID());
        Assert.assertEqualsString("RoomWBath", reservation.getRoomType());
        try {
            Assert.assertEqualsDate(dateFormat.parse("Jan 02, 2025"), dateFormat.parse(reservation.getReservationStartDate()));
            Assert.assertEqualsDate(dateFormat.parse("Jan 05, 2025"), dateFormat.parse(reservation.getReservationEndDate()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    // public UUID getReservationID() ;
    static public void testUUID(Reservation reservation) {
        System.out.println("UUID Tests");
        Reservation r2 = new Reservation(1, "RoomWBath", "Jan 02, 2025", "Jan 05, 2025");
        Assert.assertNotEqualsUUID(reservation.getReservationID(), r2.getReservationID());
    }

    // public Date getReservationDate() ;
    static public void testReservationDate(Reservation reservation) {
        System.out.println("Reservation Date Tests");
        try {
            Date d = new Date();
            Assert.assertEqualsInt(1, areDatesSimilar(d, reservation.getReservationDate()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    // public int getGuestID()  ;
    static public void testGuestID(Reservation reservation) {
        System.out.println("Guest ID Tests");
        Assert.assertEqualsInt(1, reservation.getGuestID());
        int newGuestID = reservation.getGuestID() + 1;
        reservation.setGuestID(newGuestID);
        Assert.assertEqualsInt(newGuestID, reservation.getGuestID());
    }


    // try {
    //     System.out.println("Testing Calculate: " + calculateReservationNumberOfDays(reservation));
       
    //     double price = (calculateReservationNumberOfDays(reservation) * roomTypes.get(reservation.getRoomType()));
    //     Assert.assertEqualsDouble(price, reservation.calculateReservationBillAmount());
    // } catch (Exception e) {
    //     System.out.println("Exception during calculation\n");
    //     e.printStackTrace();
    // }




    // public String getRoomType() ;

    // public String getReservationStartDate() ;

    // public String getReservationEndDate() ;

    // public void setGuestID(int var1) ;

    // public void setRoom(String var1) ;

    // public void setReservationStartDate(String var1) ;

    // public void setReservationEndDate(String var1) ;

    // public long calculateReservationNumberOfDays() throws Exception ;

    // public double calculateReservationBillAmount() throws Exception ;

}
