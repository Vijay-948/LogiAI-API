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
public class ReportRequestDto {
  Date fromDate;
  Date toDate;
  Integer userId;
  Integer operations;
}
