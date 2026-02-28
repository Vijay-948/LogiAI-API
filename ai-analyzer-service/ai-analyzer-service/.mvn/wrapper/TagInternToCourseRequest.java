package com.peopletech.fractionable.dto.request;

import java.util.Date;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class TagInternToCourseRequest {
  private Integer courseId;
  private Integer UserId;
  private Integer ManagerId;
  private Date startDate;
  private Date endDate;
  private String Status;
  private Integer percentage;
}
