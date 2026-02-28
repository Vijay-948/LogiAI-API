package com.peopletech.fractionable.dto.request;

import com.peopletech.fractionable.dto.LookupDto;
import java.util.List;
import lombok.Data;

@Data
public class GetQuestionRequestDto {
  private Integer questionnaireType;
  private List<LookupDto> skills;
}
