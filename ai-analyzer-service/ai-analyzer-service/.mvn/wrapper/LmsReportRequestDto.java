package com.peopletech.fractionable.dto.request;

import java.util.Date;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class LmsReportRequestDto {
  private Integer userId;
  private Date fromDate;
  private Date toDate;
}
