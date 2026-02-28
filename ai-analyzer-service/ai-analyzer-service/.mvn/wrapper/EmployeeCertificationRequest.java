package com.peopletech.fractionable.dto.request;

import java.util.Date;
import lombok.Data;

@Data
public class EmployeeCertificationRequest {
  private Integer employeeId;

  private String certificationName;

  private Integer certificationAreaId;

  private Date completeDate;

  private Date expiryDate;

  private String examCode;

  private String certificationNumber;
}
