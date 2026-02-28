package com.peopletech.fractionable.dto.request;

import java.util.Date;
import java.util.List;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class TagBulkEmployeesCourseRequest {
  private List<Integer> employeeIds;
  private Integer managerId;
  private Integer levelId;
  private Integer techStackId;
  private List<Integer> courseId;
  private Date startDate;
  private Date endDate;
}
