import java.util.*;
import java.text.SimpleDateFormat;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

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
        String file = "testcases.csv";
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                // Each line is a test case, split by comma if needed
                String[] values = line.split("!");
                // Process values as needed
                int custId = Integer.parseInt(values[0].trim());
                executeTests(custId, values[1].trim(), values[2].trim(), values[3].trim());
                System.out.println();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static public void executeTests(int custId, String roomType, String startDate, String endDate) {
        System.out.println("Testing Reservation " + custId);
        System.out.printf("Arguments: %d, %s, %s, %s\n", custId, roomType, startDate, endDate);
        System.out.println("------------------------------------------------------------");
        Reservation reservation = testConstruction(custId, roomType, startDate, endDate);
        testUUID(reservation);
        testReservationDate(reservation);
        testGuestID(reservation, custId);
        testRoomType(reservation, roomType);
        testReservationStartDate(reservation, startDate);
        testSetReservationStartDate(reservation, startDate);
        testReservationEndDate(reservation, endDate);
        testSetReservationEndDate(reservation, endDate);
        testSetGuestID(reservation, custId);
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

    static public Reservation testConstruction(int custId, String roomType, String startDate, String endDate) {
        System.out.println("---> Construction Tests");
        Reservation reservation = new Reservation(custId, roomType, startDate, endDate);
            Assert.assertEqualsInt(reservation.getGuestID(), custId);
            Assert.assertEqualsString(reservation.getRoomType(), roomType);
            try {
                Assert.assertEqualsDate(dateFormat.parse(reservation.getReservationStartDate()), dateFormat.parse(startDate));
                Assert.assertEqualsDate(dateFormat.parse(reservation.getReservationEndDate()), dateFormat.parse(endDate));
            } catch (Exception e) {
                e.printStackTrace();
            }

        return reservation;
    }
    
    // public UUID getReservationID() ;
    static public void testUUID(Reservation reservation) {
        System.out.println("---> UUID Tests");
        Reservation r2 = new Reservation(1, "RoomWBath", "Jan 02, 2025", "Jan 05, 2025");
        Assert.assertNotEqualsUUID(r2.getReservationID(), reservation.getReservationID());
    }

    // public Date getReservationDate() ;
    static public void testReservationDate(Reservation reservation) {
        System.out.println("---> Reservation Date Tests");
            try {
                Date d = new Date();
                Assert.assertEqualsInt(1, areDatesSimilar(reservation.getReservationDate(), d));
            } catch (Exception e) {
                e.printStackTrace();
            }
    }
    
    // public int getGuestID()  ;
    static public void testGuestID(Reservation reservation, int oriID) {
        System.out.println("---> Guest ID Tests");
        Assert.assertEqualsInt(reservation.getGuestID(), oriID);
    }
    
    // public String getRoomType() ;
    static public void testRoomType(Reservation reservation, String oriType) {
        System.out.println("---> Room Type Tests");
        Assert.assertEqualsString(reservation.getRoomType(), oriType);
        String newRoomType = "NormalRoom";
        if(reservation.getRoomType().equals(newRoomType)) {
            newRoomType = "RoomWBath";
        }
        reservation.setRoom(newRoomType);
        Assert.assertEqualsString(reservation.getRoomType(), newRoomType);
    }

    // public String getReservationStartDate() ;
    static public void testReservationStartDate(Reservation reservation, String oriStartDate) {
        System.out.println("---> Reservation Start Date Tests");
        Assert.assertEqualsString(reservation.getReservationStartDate(), oriStartDate);
    }

    static public void testSetReservationStartDate(Reservation reservation, String oriStartDate) {
        System.out.println("---> Reservation Start Date Tests");
        Assert.assertEqualsString(reservation.getReservationStartDate(), oriStartDate);
        try {
            Date d = dateFormat.parse(oriStartDate);
            Calendar c = Calendar.getInstance();
            c.setTime(d);
            c.add(Calendar.DATE, -1);
            reservation.setReservationStartDate(dateFormat.format(c.getTime()));
            Assert.assertEqualsString(reservation.getReservationStartDate(), dateFormat.format(c.getTime()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    // public String getReservationEndDate() ;
    static public void testReservationEndDate(Reservation reservation, String oriEndDate) {
        System.out.println("---> Reservation End Date Tests");
        Assert.assertEqualsString(reservation.getReservationEndDate(), oriEndDate);
    }

    static public void testSetReservationEndDate(Reservation reservation, String oriEndDate) {
        System.out.println("---> Reservation End Date Tests");
        Assert.assertEqualsString(reservation.getReservationEndDate(), oriEndDate);
        try {
            Date d = dateFormat.parse(oriEndDate);
            Calendar c = Calendar.getInstance();
            c.setTime(d);
            c.add(Calendar.DATE, 2);
            reservation.setReservationEndDate(dateFormat.format(c.getTime()));
            Assert.assertEqualsString(reservation.getReservationEndDate(), dateFormat.format(c.getTime()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // public void setGuestID(int var1) ;
    static public void testSetGuestID(Reservation reservation, int oriID) {
        System.out.println("---> Guest ID Tests (" + oriID + ")");
        int newGuestID = reservation.getGuestID() + 1;
        reservation.setGuestID(newGuestID);
        Assert.assertEqualsInt(reservation.getGuestID(), newGuestID);
    }

    // public void setRoom(String var1) ;

    // public void setReservationStartDate(String var1) ;

    // public void setReservationEndDate(String var1) ;

    // public long calculateReservationNumberOfDays() throws Exception ;

    // public double calculateReservationBillAmount() throws Exception ;


    // try {
    //     System.out.println("Testing Calculate: " + calculateReservationNumberOfDays(reservation));
       
    //     double price = (calculateReservationNumberOfDays(reservation) * roomTypes.get(reservation.getRoomType()));
    //     Assert.assertEqualsDouble(price, reservation.calculateReservationBillAmount());
    // } catch (Exception e) {
    //     System.out.println("Exception during calculation\n");
    //     e.printStackTrace();
    // }
}
