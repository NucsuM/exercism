class Acronym
    def self.abbreviate(long)
        long.scan(/\b\w/).join.upcase
    end
end