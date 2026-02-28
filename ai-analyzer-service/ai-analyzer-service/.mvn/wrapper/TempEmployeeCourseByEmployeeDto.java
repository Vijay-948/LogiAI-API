package com.peopletech.fractionable.dto.request;

import java.util.Date;
import lombok.Data;

@Data
public class TempEmployeeCourseByEmployeeDto {

  private Integer internId;

  private Integer courseId;

  private Date actualEndDate;

  private Integer percentage;

  private String status;
}
